import scipy.misc
import numpy as np

class Curva():
    def __init__(self, list_t: list, funcX, funcY) -> None:
        self.list_t = list_t
        self.funcX = funcX
        self.funcY = funcY

        self.__x_t = {}
        self.__y_t = {}
        self.__lista_x = []
        self.__lista_y = []
        self.__lista_xl = []
        self.__lista_yl = []
        self.__lista_xl_t = {}
        self.__lista_yl_t = {}
        self.__pxs = []
        self.__pys = []
        self.__horTg = {
            't': [],
            'X': [],
            'Y': []
        }
        self.__vertTg = {
            't': [],
            'X': [],
            'Y': []
        }
        self.__intersec = {}

    def printaIntersec(self) -> None:
        print("Pontos de auto-interseção (sem duplicatas):")
        for t_val, coord in self.__intersec.items():
            print(f"{t_val}, Coordenadas: X = {coord['X']:.3f}, Y = {coord['Y']:.3f}")

    def printaHorTg(self) -> None:
        print('Pontos em que a tangente é horizontal:')
        for i in range(len(self.__horTg['X'])):
            print(f"t = {self.__horTg['t'][i]:.3f}, X = {self.__horTg['X'][i]:.3f}, Y = {self.__horTg['Y'][i]:.3f}")

    def printaVertTg(self) -> None:
        print('Pontos em que a tangente é vertical:')
        for i in range(len(self.__vertTg['X'])):
            print(f"t = {self.__vertTg['t'][i]:.3f}, X = {self.__vertTg['X'][i]:.3f}, Y = {self.__vertTg['Y'][i]:.3f}")

    def derivaX(self, funcX, t: float) -> float:     
        return scipy.misc.derivative(funcX, t, dx=1e-6)

    def derivaY(self, funcY, t: float) -> float:     
        return scipy.misc.derivative(funcY, t, dx=1e-6)
        
    def verificaTg(self) -> None:
        for i in range(len(self.list_t) - 1):
            x1 = self.__lista_xl[i]
            x2 = self.__lista_xl[i + 1]
            y1 = self.__lista_yl[i]
            y2 = self.__lista_yl[i + 1]
            primeiro = False
            # if i == 0:
            #     primeiro = True
            self.metodoBissecX(i, y1, y2, primeiro)
            self.metodoBissecY(i, x1, x2, primeiro)

    def metodoBissecX(self, i, y1, y2, primeiro) -> None:
        if primeiro:
            y3 = self.__lista_yl[i - 1]
            if y1 * y3 < 0 or y1 * y2 < 0:
                self.__horTg['t'].append(self.list_t[i])
                self.__horTg['X'].append(self.__x_t[self.list_t[i]]) 
                self.__horTg['Y'].append(self.__y_t[self.list_t[i]])
        elif y1 * y2 < 0:
            self.__horTg['t'].append(self.list_t[i])
            self.__horTg['X'].append(self.__x_t[self.list_t[i]]) 
            self.__horTg['Y'].append(self.__y_t[self.list_t[i]])

    def metodoBissecY(self, i, x1, x2, primeiro) -> None:
        if primeiro:
            x3 = self.__lista_xl[i - 1]
            if x1 * x3 < 0 or x1 * x2 < 0:
                self.__vertTg['t'].append(self.list_t[i])
                self.__vertTg['X'].append(self.__x_t[self.list_t[i]])
                self.__vertTg['Y'].append(self.__y_t[self.list_t[i]])
        elif x1 * x2 < 0:
            self.__vertTg['t'].append(self.list_t[i])
            self.__vertTg['X'].append(self.__x_t[self.list_t[i]])
            self.__vertTg['Y'].append(self.__y_t[self.list_t[i]])

    def verificaIntersec(self, x1, x2, x3, x4, y1, y2, y3, y4) -> tuple:
        try:
            m1 = (y2 - y1) / (x2 - x1)
            m2 = (y4 - y3) / (x4 - x3)
        except ZeroDivisionError:
            return None  # Evita divisão por zero se as retas são verticais

        # Verifica se as retas são paralelas
        if abs(m1 - m2) < 1e-6:
            return None  # Retas são praticamente paralelas, sem interseção

        # Calcula ponto de interseção
        px = (m1 * x1 - m2 * x3 + y3 - y1) / (m1 - m2)
        py = m1 * (px - x1) + y1

        # Verifica se o ponto está dentro dos segmentos
        if ((px >= min(x1, x2) and px <= max(x1, x2)) and
            (px >= min(x3, x4) and px <= max(x3, x4))):
            return px, py
        return None

    def determinaIntersec(self) -> None:    
        dict_aux = {}
        for i in range(len(self.__lista_x) - 1):
            for j in range(i - 1):
                # Calcula ponto de interseção, se existir
                xs_ys = self.verificaIntersec(
                    self.__lista_x[i], self.__lista_x[i + 1],
                    self.__lista_x[j], self.__lista_x[j + 1],
                    self.__lista_y[i], self.__lista_y[i + 1],
                    self.__lista_y[j], self.__lista_y[j + 1]
                )
                if xs_ys:
                    px, py = xs_ys
                    # Armazena o ponto e valor de t sem duplicatas
                    if (px, py) not in self.__intersec.values():
                        self.__pxs.append(px)
                        self.__pys.append(py)
                        self.__intersec[f't: {self.list_t[i]:.3f}'] = {'X': px, 'Y': py}
                        dict_aux[f'X: {px:.3f}'] = f'Y: {py:.3f}'

    def fazPontos(self) -> None:
        for t in self.list_t:
            self.__lista_x.append(self.funcX(t=t))
            self.__lista_y.append(self.funcY(t=t))

            self.__lista_xl.append(self.derivaX(funcX=self.funcX, t=t))
            self.__lista_yl.append(self.derivaY(funcY=self.funcY, t=t))

            self.__x_t[t] = self.funcX(t=t)
            self.__y_t[t] = self.funcY(t=t)

            self.__lista_xl_t[t] = self.derivaX(funcX=self.funcX, t=t)
            self.__lista_yl_t[t] = self.derivaY(funcY=self.funcY, t=t)
    

    def run(self) -> None:
        self.fazPontos()
        self.determinaIntersec()
        self.verificaTg()
        self.printaIntersec()
        self.printaHorTg()
        self.printaVertTg()
