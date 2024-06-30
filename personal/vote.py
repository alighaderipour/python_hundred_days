#vote
pez = 10415991
jalili = 9473298
ghalibaf= 3383340
poor= 206397
s1 = pez + jalili+ghalibaf+poor
summ = 24535155
bateleh = summ - s1
print('bateleh: ', bateleh)




pez_darsad = (pez / summ) * 100
jal_darsad = (jalili / summ) * 100
gha_darsad = (ghalibaf / summ) * 100
por_darsad = (poor / summ) * 100
bat_darsad = (bateleh / summ) * 100

print(f'pez =',round(pez_darsad, 2) , '%')
print(f'jal =',round(jal_darsad, 2) , '%' )
print(f'gha =',round(gha_darsad, 2) , '%')
print(f'por = ',round(por_darsad, 2) , '%')
print(f'bat = ',round(bat_darsad, 2) , '%')
#print(pez_darsad +jal_darsad +  gha_darsad + por_darsad + bat_darsad)

