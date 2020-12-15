from modules.PuzzlesAPI import PuzzleInput

url = 'https://adventofcode.com/2020/day/8/input'

input_conn = PuzzleInput(url)
soup = input_conn.get_puzzle_input()

def get_index_positions_by_condition(list_of_elems, condition):
  ''' Returns the indexes of items in the list that returns True when passed
  to condition() '''
  index_of_flipp_actions_list = []
  for i in range(len(list_of_elems)):
      if condition(list_of_elems[i]) == True:
          index_of_flipp_actions_list.append(i)
  return index_of_flipp_actions_list

index_of_actions_to_flip_list = get_index_positions_by_condition(soup, lambda x : (x.split()[0] == "jmp") or (x.split()[0] == "nop"))

class CodeRunner:
  def __init__ (self, *args, **kwargs): #(.., params)
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
  
  def flip(self, action_type):
    if action_type == 'nop':
      return 'jmp'  
    elif action_type == 'jmp':
      return 'nop'
    else:
      return action_type

  def step_forward(self, soup):
    # print(soup[self.last_position].split())
    action_type = soup[self.last_position].split()[0]
    action_value = int(soup[self.last_position].split()[1])
                       
    if action_type == "acc":
      self.accumulator += action_value
      self.last_position +=1
    elif action_type == "jmp":
      self.last_position += action_value
    else:
      self.last_position +=1 

    return (self.last_position, self.accumulator)
  
  def exactly_one_instruction_changer(self):
    soup = self.args[0]
    for i in range(len(soup)):
      new_soup = soup.copy()
      action_type = soup[i].split()[0]

      if i in index_of_actions_to_flip_list:
        action_type = self.flip(action_type)
        new_soup[i] = action_type + ' ' + soup[i].split()[1]
        self.corrected_row_index = i
        yield new_soup

  def main(self, params):

    if params.get('puzzle_part') == 2:
      generator = self.exactly_one_instruction_changer()
      for i in generator:
        soup = i 
        # print(soup)
        self.last_position = 0
        self.accumulator = 0 
        self.list_of_visited_rows = []
        while self.last_position <= (len(soup)-1):
          if self.last_position in self.list_of_visited_rows:
            break
          self.list_of_visited_rows.append(self.last_position)
          data_tuple = self.step_forward(soup)
        if not (self.last_position <= (len(soup)-1)):
          print(f"correct accumulator sum - {data_tuple[1]} \ncorrected row index - {self.corrected_row_index}")
    
    elif params.get('puzzle_part') == 1:
        soup = obj.args[0]
        self.last_position = 0
        self.accumulator = 0 
        self.list_of_visited_rows = []
        while self.last_position <= (len(soup)-1):
          if self.last_position in self.list_of_visited_rows:
            break
          self.list_of_visited_rows.append(self.last_position)
          data_tuple = self.step_forward(soup)
        print(f"accumulator sum - {data_tuple[1]}")


if __name__ == "__main__":
  
  initial_conditions = dict(accumulator = 0, corrected_row_index = 0, list_of_visited_rows = [], last_position = 0)
  params = {'puzzle_part':1}

  obj = CodeRunner(soup, **initial_conditions)
  # soup --> obj.args[0]
  obj.main(params)


