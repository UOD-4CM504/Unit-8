
def write_nums(n):
  nums = [f"{x}\n" for x in range(1,n+1)]
  with open("nums.txt", "w") as f:
    f.writelines(nums)

if __name__ == "__main__":
  write_nums(10)
  # writes out the first 10 even numbers to evens.txt