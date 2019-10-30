Larg = float(input('Largura da parade: '))
Alt = float(input('Altura da parede: '))
Area = Larg * Alt
Tinta = Area / 2
print("Sua parede tem a dimensão de {}X{} e sua área é de {:.3f}m².".format(Larg, Alt, Area))
print('Para pintar essa parede, você precisará de {}l de tinta.'.format(Tinta))



