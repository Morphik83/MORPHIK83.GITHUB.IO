scores = [10, 50, 100, 175, 250, 400, 600, 800, 1000]
ranks = 'white yellow orange green blue brown black paneled red'.split()
BELTS = dict(zip(scores, ranks))


class NinjaBelt:

  def __init__(self, score=0):
    self._score = score
    self._last_earned_belt = None

  def _get_belt(self, new_score):
    is_new_belt_earned = False
    if new_score < 10:
      self._last_earned_belt = ''
    elif new_score > 1000:
      self._last_earned_belt = 'red'
    else:
      for index, value in enumerate(scores):
        if new_score < value:
          belt = BELTS.get(scores[index - 1]).title()
          if belt != self._last_earned_belt:
            self._last_earned_belt = belt
            is_new_belt_earned = True
          break
        elif new_score == value:
          belt = BELTS.get(scores[index])
          self._last_earned_belt = belt.title()
          is_new_belt_earned = True
          break
    return is_new_belt_earned

  @property
  def score(self):
    return self._score

  @score.setter
  def score(self, new_score):
    if isinstance(new_score, int) and new_score >= self._score:
      self._score = new_score
      if not self._get_belt(new_score):
        print(f'Set new score to {self._score}')
      else:
        print(
            f'Congrats, you earned {self._score} points obtaining the PyBites Ninja {self._last_earned_belt} Belt')
    else:
      raise ValueError

  # score = property(_get_score, _set_score)
