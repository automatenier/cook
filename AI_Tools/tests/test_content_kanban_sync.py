"""
Unit tests for content_kanban_sync.py

Tests kanban parsing, deduplication, and platform normalization.
"""

import pytest
from pathlib import Path
import sys

# Add parent dir to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from content_kanban_sync import (
    parse_kanban,
    extract_metadata,
    clean_platform,
    get_existing_titles,
)


class TestKanbanParsing:
    """Test Kanban markdown parsing."""

    def test_parse_scheduled_lane(self):
        """Extract items from Scheduled lane only."""
        kanban_md = """
## 🔍 Outlier Research

- [ ] ### [IDEA] Analyze viral reels
	**Platform:** 📸 Instagram
	**Post Date:** TBD
	**Captions:** TBD

## Scheduled

- [ ] ### [IDEA] First scheduled item
	**Platform:** 📱 TikTok
	**Post Date:** 2026-03-05
	**Captions:** Hook: Pattern Interrupt

- [ ] ### [IDEA] Second scheduled item
	**Platform:** 🎥 YouTube Short
	**Post Date:** 2026-03-06
	**Captions:** TBD
        """

        items = parse_kanban(kanban_md)

        assert len(items) == 2, "Should extract 2 items from Scheduled lane only"
        assert items[0]['title'] == 'First scheduled item'
        assert items[0]['platform'] == 'TikTok'
        assert items[0]['post_date'] == '2026-03-05'

        assert items[1]['title'] == 'Second scheduled item'
        assert items[1]['platform'] == 'YouTube Short'


    def test_parse_empty_scheduled(self):
        """Handle empty Scheduled lane gracefully."""
        kanban_md = """
## Outlier Research

- [ ] ### [IDEA] Some idea
	**Platform:** 📸 Instagram
	**Post Date:** TBD
	**Captions:** TBD

## Scheduled
        """

        items = parse_kanban(kanban_md)
        assert len(items) == 0, "Should return empty list for empty Scheduled lane"


    def test_extract_metadata(self):
        """Extract key-value pairs from metadata block."""
        metadata = """	**Platform:** 📸 Instagram
	**Post Date:** 2026-03-05
	**Captions:** Hook: Something"""

        platform = extract_metadata(metadata, 'Platform')
        post_date = extract_metadata(metadata, 'Post Date')
        captions = extract_metadata(metadata, 'Captions')

        assert platform == '📸 Instagram'
        assert post_date == '2026-03-05'
        assert captions == 'Hook: Something'


    def test_extract_missing_metadata(self):
        """Return empty string for missing metadata."""
        metadata = "	**Platform:** TikTok"

        result = extract_metadata(metadata, 'NonExistent')
        assert result == ''


class TestPlatformNormalization:
    """Test platform string cleaning."""

    def test_normalize_tiktok(self):
        """Normalize TikTok variants."""
        assert clean_platform('📱 TikTok') == 'TikTok'
        assert clean_platform('tiktok') == 'TikTok'
        assert clean_platform('TikTok') == 'TikTok'


    def test_normalize_ig_reel(self):
        """Normalize Instagram Reel variants."""
        assert clean_platform('📸 Instagram') == 'IG Reel'
        assert clean_platform('IG Reel') == 'IG Reel'
        assert clean_platform('IG Reels') == 'IG Reel'


    def test_normalize_ig_story(self):
        """Normalize Instagram Story."""
        assert clean_platform('📸 Instagram Story') == 'IG Story'
        assert clean_platform('IG Story') == 'IG Story'


    def test_normalize_youtube_short(self):
        """Normalize YouTube Short."""
        assert clean_platform('🎥 YouTube Short') == 'YouTube Short'
        assert clean_platform('YouTube Short') == 'YouTube Short'
        assert clean_platform('YT Short') == 'YouTube Short'


    def test_normalize_youtube_long(self):
        """Normalize YouTube Long."""
        assert clean_platform('YouTube Long') == 'YouTube Long'
        assert clean_platform('YT Long') == 'YouTube Long'


    def test_normalize_threads(self):
        """Normalize Threads."""
        assert clean_platform('Threads') == 'Threads'


    def test_normalize_multiple_platforms(self):
        """Handle comma/slash-separated platforms (use first)."""
        assert clean_platform('📸 Instagram / 📱 TikTok') == 'IG Reel'
        assert clean_platform('Instagram, TikTok') == 'IG Reel'


    def test_normalize_empty(self):
        """Handle empty platform."""
        assert clean_platform('') == ''
        assert clean_platform('   ') == ''


    def test_normalize_analysis(self):
        """Handle Analysis/non-posting platforms."""
        assert clean_platform('📊 Analysis') == 'Analysis'
        assert clean_platform('Analysis') == 'Analysis'


class TestDeduplication:
    """Test duplicate detection."""

    def test_existing_titles_extraction(self):
        """Extract title values from mock row data."""
        # Mock row data (each row is a tuple/list of cells)
        class MockCell:
            def __init__(self, value):
                self.value = value

        data = [
            [MockCell(1), MockCell('First Title'), MockCell('IG Reel')],
            [MockCell(2), MockCell('Second Title'), MockCell('TikTok')],
            [MockCell(3), MockCell(None), MockCell('YouTube')],  # Empty title
        ]

        titles = get_existing_titles(data)

        assert 'First Title' in titles
        assert 'Second Title' in titles
        assert None not in titles
        assert len(titles) == 2


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
