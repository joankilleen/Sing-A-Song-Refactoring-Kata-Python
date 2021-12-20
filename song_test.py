import song as Song
import pytest
REFERENCE_SONG_FILEPATH = "testdata/reference_song.txt"

@pytest.fixture
def reference_song():
    f = open(REFERENCE_SONG_FILEPATH, "r")
    return f.read()

def test_output(reference_song):
    output = Song.output()
    assert output == reference_song
    print(reference_song)
    