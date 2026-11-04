result=float(input("Enter student mark(out of 100):"))
assignment=float(input("Enter student assignment mark(out of 50):"))
tutorial1=float(input("Enter student tutorial mark 1(out of 30):"))
tutorial2=float(input("Enter student tutorial mark 2(out of 30):"))
assignment_score=(assignment/50)*20
tutorial_average=(tutorial1+tutorial2)/2
tutorial_score=(tutorial_average/30)*10
exam_score=(result/100)*70
final_score=exam_score+tutorial_score+assignment_score
print("the final score:",final_score)

