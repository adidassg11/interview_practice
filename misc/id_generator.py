#!/usr/bin/python3
from abc import ABCMeta, abstractmethod
from math import ceil, floor, log2


class ListUtils(object):
    def get_lc_idx(i):
        """ Get left child index, assumes 0-index array"""
        return 2*i + 1

    def get_rc_idx(i):
        return 2*i + 2

    def get_parent_idx(i):
        if i == 0:
            raise Exception('Node 0 has no parent')

        if i % 2 == 0:  # Get parent of right child
            return i//2 - 1
        else:  # Left child
            return i//2


class IDAllocator(metaclass=ABCMeta):
    """
        Abstract base class for ID Allocator classes
    """
    @abstractmethod
    def get_next_avail(self):
        pass

    @abstractmethod
    def release_id(self, id):
        pass


class IDAllocatorEasy(IDAllocator):
    """
        Use 2 set-based dictionary pools, faster and simpler but more memory
    """
    def __init__(self, size):
        self._size = size
        self._free_id_bank = set(map(lambda x: x, range(size)))
        self._used_id_bank = set()

    def __str__(self):
        return 'free ids: %s\nused ids: %s' % (self._free_id_bank, self._used_id_bank)

    def get_next_avail(self):
        if len(self._free_id_bank) == 0:
            raise Exception('No IDs available.')

        new_id = self._free_id_bank.pop()
        self._used_id_bank.add(new_id)
        return new_id

    def release_id(self, id_):
        self._used_id_bank.remove(id_)  # Raises key error if user gives invalid ID
        self._free_id_bank.add(id_)


class IDAllocatorCompact(IDAllocator):
    """
        A little slower but much more compact version, good for huge id pools
        using balanced binary tree of single bits, total consumption N*2-1 bits
        and O(logN) retrieval and release
        ... for now just use regular list not bitarray
    """

    def __init__(self, size):
        self._size = size

        next_power2 = 2 ** ceil(log2(self._size))  # size rounded up to nearest power 2
        self._next_power2 = next_power2
        self._unavail_bank_size = next_power2 - size
        self._avail_bank_size = next_power2*2 - self._unavail_bank_size - 1
        self._total_bank_size = self._unavail_bank_size + self._avail_bank_size

        # used to store bin tree structure for bank access
        self._id_bank = self._avail_bank_size*[1]  # real bank
        self._id_bank.extend(self._unavail_bank_size*[0])

        #self._id_bank = list(map(lambda x: x, range(self._total_bank_size)))  # test bank for print
        '''
        # Debug
        print('bank size: %s' % self._size)
        print('next_power2: %s' % next_power2)
        print('bank avail bank size: %s' % self._avail_bank_size)
        print('bank unavail bank size: %s' % self._unavail_bank_size)
        print('bank total bank size: %s' % self._total_bank_size)
        print('tree array: %s' % self._id_bank)
        '''

        # Need to find 0's and propogate them up...
        # Optimization to only try even indicies
        zeros_range = range(self._avail_bank_size, self._total_bank_size)
        for i in filter(lambda x: x % 2 == 0, zeros_range):
            self._propagate_up(i)

    def _propagate_up(self, idx):
        if idx < 0 or idx >= len(self._id_bank):
            return

        # Set current value based on child nodes
        left_child_idx = ListUtils.get_lc_idx(idx)
        right_child_idx = ListUtils.get_rc_idx(idx)
        if right_child_idx >= self._total_bank_size:
            return self._propagate_up(ListUtils.get_parent_idx(idx))

        new_value = self._id_bank[left_child_idx] or self._id_bank[right_child_idx]

        # See if value changed. If not, no need to continue propagating
        if self._id_bank[idx] == new_value:
            return

        self._id_bank[idx] = new_value

        # Only keep propagating if we haven't reached final parent
        if idx > 0:
            return self._propagate_up(ListUtils.get_parent_idx(idx))

    def __str__(self):
        """
            Print id bank in the following format:

                     0
                1         2
              3  4     5     6
            7 8 9 10 11 12 13 14
            This does not account for digit widths (because bank is all 0 or 1)
        """
        ret_str = ''

        bank_width = 1
        bank_start_idx = 0
        num_pad_spaces = self._next_power2 // 2
        num_levels = ceil(log2(self._total_bank_size))

        for i in range(num_levels):
            pre_spaces = ' ' * max(0, 2**(num_levels-i-1))  # Magic math, spaces before #s
            mid_spaces = ' ' * max(0, 2**(num_levels-i)-1)  # More math, spaces between #s
            num_slice = self._id_bank[bank_start_idx:bank_start_idx+bank_width]
            nums = mid_spaces.join(map(lambda x: str(x), num_slice))
            print('%s%s' % (pre_spaces, nums))
            bank_start_idx += bank_width
            bank_width = bank_width * 2

        return ret_str

    def get_next_avail(self):
        pass

    def release_id(self, id_):
        pass

'''
id_alloc = IDAllocatorEasy(5)
print(id_alloc.get_next_avail())
print(id_alloc)
print(id_alloc.get_next_avail())
print(id_alloc.get_next_avail())
id_alloc.get_next_avail()
print(id_alloc)

id_alloc.release_id(3)
id_alloc.release_id(10)
print(id_alloc)
'''

id_alloc = IDAllocatorCompact(9)
print(id_alloc)
