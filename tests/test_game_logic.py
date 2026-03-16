from logic_utils import check_guess, parse_guess, update_score, get_range_for_difficulty


def test_winning_guess():
    # if secret is 50 and guess is 50, should be a win
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"


def test_guess_too_high():
    # if secret is 50 and guess is 60, hint should be Too High
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"


def test_guess_too_low():
    # if secret is 50 and guess is 40, hint should be Too Low
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"


def test_parse_guess_valid():
    # a normal number string should parse correctly
    ok, value, err = parse_guess("42")
    assert ok == True
    assert value == 42
    assert err is None


def test_parse_guess_empty():
    # empty input should return an error
    ok, value, err = parse_guess("")
    assert ok == False
    assert err == "Enter a guess."


def test_parse_guess_not_a_number():
    # a word should return an error
    ok, value, err = parse_guess("abc")
    assert ok == False
    assert err == "That is not a number."


def test_score_increases_on_win():
    # winning should add points to score
    new_score = update_score(0, "Win", 1)
    assert new_score > 0


def test_score_decreases_on_wrong_guess():
    # wrong guess should subtract points
    new_score = update_score(50, "Too High", 1)
    assert new_score < 50


def test_hard_range_is_harder_than_normal():
    # hard mode should have a bigger range than normal
    _, normal_high = get_range_for_difficulty("Normal")
    _, hard_high = get_range_for_difficulty("Hard")
    assert hard_high > normal_high