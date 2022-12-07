from modules.PuzzlesAPI import PuzzleInput

url = 'http://adventofcode.com/2022/day/1/input'

input_conn = PuzzleInput(url)
soup = input_conn.get_puzzle_input()

class CodeRunner:
  # the lack of a return type is the same as -> None
  def __init__ (self, *args, **kwargs) -> None:
    # args is a tuple of positional arguments,
    # because the parameter name has * prepended.
    if args: # If args is not empty.
        self.args = args
    # kwargs is a dictionary of keyword arguments,
    # because the parameter name has ** prepended.
    if kwargs: # If kwargs is not empty.
      for (key, value) in kwargs.items():
        setattr(self, key, value)
    # params = {'puzzle_part': 1} The .get method will return a key from a dictionary, but if no key is found it will return None
    # self.puzzle_part = params.get('puzzle_part')
    pass

  def summarize_calories(self):
    """
    map converts sublist of strings to list of integers
    then sum summarizes all elements in sublist
    """
    return [sum(list(map(int, element.split("\n")))) for element in self.soup]

  def main (self, arguments_list: list):
    """
    main function to run in standalone regime
    just returns max value from list
    """
    # arguments_list.index(68802)
    # arguments_list[20]
    print(max(arguments_list))
    return  max(arguments_list)



if __name__ == "__main__":
  
  # initial_conditions = dict(accumulator = 0, corrected_row_index = 0, list_of_visited_rows = [], last_position = 0)
  # params = {'puzzle_part':2}

  kwargs = {"soup": soup}

  obj = CodeRunner(soup, **kwargs)
  # soup --> obj.args[0]
  # soup = obj.kwargs['soup']
  obj.main(obj.summarize_calories())