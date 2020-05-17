class Solutuon:
    def zigzagLevelOrder(self, root):
        if root is None:
            return None
        res = []
        level = 0
        