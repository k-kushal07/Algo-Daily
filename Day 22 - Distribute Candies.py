def distri_candy(self, candy):
        if len(set(candy)) >= len(candy)//2:
            return len(candy)//2
        else:
            return len(set(candy))
