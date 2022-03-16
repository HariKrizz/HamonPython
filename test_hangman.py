import os
import hangman
def test_get_word_no_punctuation():
    with open("/tmp/words.txt", "w") as f:
        f.write("elephant\n")
        f.write("car's\n")
        f.write("planes's\n")
        f.write("amazing!!!\n")
    for _ in range(100):
        word = hangman.get_word("/tmp/words.txt")
        assert word == "elephant"
    os.unlink("/tmp/words.txt")

def test_get_word_no_proper_nouns():
    with open("/tmp/words.txt", "w") as f:
        f.write("elephant\n")
        f.write("Noufal\n")
        f.write("John\n")
        f.write("Simon\n")
    for _ in range(100):
        word = hangman.get_word("/tmp/words.txt")
        assert word == "elephant"
    os.unlink("/tmp/words.txt")

def test_get_word_min_length():
    with open("/tmp/words.txt", "w") as f:
        f.write("elephant\n")
        f.write("egg\n")
        f.write("an\n")
        f.write("fun\n")
    for _ in range(100):
        word = hangman.get_word("/tmp/words.txt")
        assert word == "elephant"
    os.unlink("/tmp/words.txt")

def test_mask_word_single_letter():
    secret_word = "elephant"
    guesses= ["l"]
    ret =hangman.mask_word(secret_word,guesses)
    assert ret == "-l------"
   
def test_mask_word_mulitple_letter():
    secret_word = "elephant"
    guesses= ["e"]
    ret =hangman.mask_word(secret_word,guesses)
    assert ret == "e-e-----"

def test_mask_word_mix_letter():
    secret_word = "elephant"
    guesses= ["e","l","y"]
    ret =hangman.mask_word(secret_word,guesses)
    assert ret == "ele-----"

def test_game_status_not_guessed():
    secret_word = "elephant"
    guesses = []
    remaining_turns = 8
    status = hangman.game_status(secret_word, guesses, remaining_turns)
    assert status == """Word:--------
    Guesses:
    Remaining Turns:8
    """
 
# def test_create_status_normal():
#     secret_word = "elephant"
#     guesses = ["a", "x", "h"]
#     remaining_turns = 7
#     ret = hangman.game_status(secret_word, guesses, remaining_turns)
#     assert ret == """Word:----ha--
#     Guesses:a x h
#     Remaining Turns:7
#     """

# def test_play_correct_guess():
#     secret_word = "computer"
#     guesses = []
#     remaining_turns = 8
#     guess = "e"
#     remaining_turns, repeat, finished = hangman.play_round(secret_word, guesses, guess, remaining_turns)
#     assert guesses == ["e"]
#     assert remaining_turns == 8
#     assert repeat == False
#     assert finished == False

# def test_play_round_correct_repeat():
#     secret_word = "nvidia"
#     guesses = ["i"]
#     remaining_turns = 6
#     guess = "i"
#     remaining_turns, repeat, finished = hangman.play_round(secret_word, guesses, guess, remaining_turns)
#     assert guesses == ["i"]
#     assert remaining_turns == 6
#     assert repeat == True
#     assert finished == False

# def test_play_round_correct_wrong():
#     secret_word = "computer"
#     guesses = ["e"]
#     remaining_turns = 8
#     guess = "x"
#     remaining_turns, repeat, finished = hangman.play_round(secret_word, guesses, guess, remaining_turns)
#     assert guesses == ["e", "x"]
#     assert remaining_turns == 7
#     assert repeat == False
#     assert finished == False

# def test_play_round_correct_complete():
#     secret_word = "thunder"
#     guesses = ["t", "h", "u", "n", "d","e","r"]
#     remaining_turns = 7
#     guess = ""
#     remaining_turns, repeat, finished = hangman.play_round(secret_word, guesses, guess, remaining_turns)
#     assert finished == True