class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # Stack to store surviving asteroids
        stack = []

        # Process each asteroid in order
        for asteroid in asteroids:
            alive = True  # Whether the current asteroid survives

            # Collision occurs ONLY when:
            # - stack is not empty
            # - top of stack > 0  (moving right)
            # - asteroid < 0      (moving left)
            # - alive is True
            while alive and stack and stack[-1] > 0 and asteroid < 0:

                # CASE 1: Incoming asteroid is bigger → pop the stack asteroid
                if abs(asteroid) > abs(stack[-1]):
                    stack.pop()

                # CASE 2: Same size → both explode
                elif abs(asteroid) == abs(stack[-1]):
                    stack.pop()
                    alive = False  # current asteroid is destroyed

                # CASE 3: Incoming asteroid is smaller → it gets destroyed
                else:
                    alive = False  # top stays, current dies

            # If the asteroid survived collisions, add it to the stack
            if alive:
                stack.append(asteroid)

        # Final surviving asteroids remain in the stack
        return stack
