class Solution(object):
    def sortTheStudents(self, score, k):
        my_list = []
        for i in range(len(score)):
            my_list.append((score[i][k], score[i]))
        my_list.sort(reverse=True)
        final_matrix = []
        for j, k in my_list:
            final_matrix.append(k)
        return final_matrix


        
