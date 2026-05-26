class AccessCounterService:
    def calculate_accesses(self, acess: int) -> int:
        count_per_access = 50
        return acess * count_per_access
