height=input('身長(cm)>>')
height_m=float(height)/100
weight=float(input('体重(kg)>>'))
bmi=weight/height_m**2
print(f'身長{height}cm,体重{weight}kgのBMIは{bmi:.1f}です')

