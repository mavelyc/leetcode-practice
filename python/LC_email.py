#Leet code unique email address

class Solution():
    def numUniqueEmails(self, emails):
        diff = []
        flag = 0
        add = 0
        for i in emails:
            tmp = ""
            for j in i:
                if j == "+":
                    flag = 1
                if j == "@":
                    flag = 2
                if flag == 0:
                    if j != ".":
                        tmp+=j
                if flag == 2:
                    tmp+=j
            flag = 0
            for each in diff:
                if tmp == each:
                    add = 1
            if add == 0:
                diff.append(tmp)
            add = 0

        print diff


test = ["hel.l+o@gm.ail.com","hel.l+o@gm.ail.com","he.l+o@gm.ail.com"]
obj = Solution()
obj.numUniqueEmails(test)