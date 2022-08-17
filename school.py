class School:

    # class attributes
    city =  'New York City'
    
    def __init__(self, dbn, name, reading_avg, math_avg, writing_score, boro, total_students,
                 attendance_rate):

        # instance attributes
        self.dbn = dbn
        self.name = name
        self.reading_avg = reading_avg
        self.math_avg = math_avg
        self.writing_score = writing_score
        self.boro = boro
        self.total_students = total_students
        self.attendance_rate = attendance_rate

    def total_score(self):
        total_score = float(self.math_avg + self.reading_avg + self.writing_score)

        return total_score

    def avg_student_attendance(self):
        avg_student_attendance = self.total_students*self.attendance_rate

        return avg_student_attendance

    def max_score(self):
        scores = [self.reading_avg, self.math_avg, self.writing_score]

        max_score =  scores[0]
        for score in scores:
            if score > max_score:
                max_score = score

        return max_score
    
        

