#5. Read about the Tower of Hanoi algorithm. Write a program to implement it.
def tower_of_hanoi(n, from_rod, to_rod, aux_rod):
    if n == 1:
        print("Move disk 1 from rod", from_rod, "to rod", to_rod)
        return
    tower_of_hanoi(n-1, from_rod, aux_rod, to_rod)
    print("Move disk", n, "from rod", from_rod, "to rod", to_rod)
    tower_of_hanoi(n-1, aux_rod, to_rod, from_rod)

# example usage
num_discs = 3
tower_of_hanoi(num_discs, 'A', 'C', 'B')