# área das importações:
import cv2
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QImage, QPixmap
from cvzone.HandTrackingModule import HandDetector
import math

# classe da programação por trás da aplicação:
class Processamento():
    # função de inicialização da classe:
    def __init__(self, tela, video, informacao, identificada, tituloQtde, numeroDedos):
        super().__init__()

        # variaveis da classe relativa a classe anterior:
        self.tela = tela
        self.video = video
        self.informacao = informacao
        self.identificada = identificada
        self.tituloQtde = tituloQtde
        self.numeroDedos = numeroDedos

        # abre a camera padrão:
        self.webCam = cv2.VideoCapture(0)

        # variavel que detecta a mão:
        self.detectorHand = HandDetector(mode=True, maxHands=1, detectionCon=0.75, minTrackCon=0.75)

        # timer que atualiza o frame do video:
        timer_video = QTimer(tela)
        timer_video.timeout.connect(self.atualizaFrame)
        timer_video.start(1)

        # chama a função de sem mão para deixar os campos certos invisiveis:
        self.semMao()
    
    # define a visibilidade dos campos para caso não tenha uma mão:
    def semMao(self):
        self.informacao.setVisible(True)
        self.identificada.setVisible(False)
        self.tituloQtde.setVisible(False)
        self.numeroDedos.setVisible(False)
    
    # define a visibilidade dos campos para caso tenha uma mão:
    def comMao(self):
        self.informacao.setVisible(False)
        self.identificada.setVisible(True)
        self.tituloQtde.setVisible(True)
        self.numeroDedos.setVisible(True)    

    # calcula a distancia entre dois pontos da mão:
    def distance(self, p1, p2):
        x1, y1, z1 = p1
        x2, y2, z2 = p2
        distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)
        return distancia
    
    # verifica se o dedo indicador está em pé:
    def distanciaIndicador(self, pontos_mao):
        ponta = pontos_mao[8]
        base = pontos_mao[5]
        distancia = self.distance(ponta, base)
        distancia = round(distancia, 2)
        if distancia > 100:
            # print("Indicador em pé")
            return 1
        else:
            # print("Indicador deitado!")
            return 0

    # verifica se o dedo medio está em pé:
    def distanciaMedio(self, pontos_mao):
        ponta = pontos_mao[12]
        base = pontos_mao[9]
        distancia = self.distance(ponta, base)
        distancia = round(distancia, 2)
        if distancia > 100:
            # print("Medio em pé")
            return 1
        else:
            # print("Medio deitado!")
            return 0

    # verifica se o dedo anelar está em pé:
    def distanciaAnelar(self, pontos_mao):
        ponta = pontos_mao[16]
        base = pontos_mao[13]
        distancia = self.distance(ponta, base)
        distancia = round(distancia, 2)
        if distancia > 100:
            # print("Anelar em pé")
            return 1
        else:
            # print("Anelar deitado!")
            return 0

    # verifica se o dedo mindinho está em pé:
    def distanciaMindinho(self, pontos_mao):
        ponta = pontos_mao[20]
        base = pontos_mao[17]
        distancia = self.distance(ponta, base)
        distancia = round(distancia, 2)
        if distancia > 100:
            # print("Mindinho em pé")
            return 1
        else:
            # print("Mindinho deitado!")
            return 0

    # verifica se o dedão está em pé:
    def distanciaDedao(self, pontos_mao):
        ponta = pontos_mao[4]
        base = pontos_mao[0]
        distancia = self.distance(ponta, base)
        distancia = round(distancia, 2)
        if distancia > 180:
            # print("Dedao em pé")
            return 1
        else:
            # print("Dedao deitado!")
            return 0
    
    # função que atualiza o frame do video da camera:
    def atualizaFrame(self):
        # captura o frame da camera:
        sucesso, frame = self.webCam.read()

        # if que verifica se a camera foi aberta com sucesso:
        if sucesso:
            # redimensiona o video:
            frame = self.tamanhoWebCam(frame) # chama a função que define o tamanho do video da webCam

            # inverte a camera (não é necessário isso, podendo ser essa linha apagada ou comentada!):
            frame = cv2.flip(frame, 1)

            # identifica a mão:
            hand = self.detectorHand.findHands(frame, False)

            # variavel com o número de dedos levantados:
            contadorDedos = 0

            # verifica se há uma mão:
            if hand:
                self.comMao()
                mao = hand[0]
                lmList = mao["lmList"]
                contadorDedos += self.distanciaIndicador(lmList)
                contadorDedos += self.distanciaMedio(lmList)
                contadorDedos += self.distanciaAnelar(lmList)
                contadorDedos += self.distanciaMindinho(lmList)
                contadorDedos += self.distanciaDedao(lmList)
                if contadorDedos == 0:
                    self.numeroDedos.setText("0 dedos\nlevantados")
                elif contadorDedos == 1:
                    self.numeroDedos.setText("01 dedos\nlevantados")
                elif contadorDedos == 2:
                    self.numeroDedos.setText("02 dedos\nlevantados")
                elif contadorDedos == 3:
                    self.numeroDedos.setText("03 dedos\nlevantados")
                elif contadorDedos == 4:
                    self.numeroDedos.setText("04 dedos\nlevantados")
                elif contadorDedos == 5:
                    self.numeroDedos.setText("05 dedos\nlevantados")
            else:
                self.semMao()

            # converte o frame para um formato RGB:
            rgbFrame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

            # cria o QImage do frame:
            h, w, ch = rgbFrame.shape
            image = QImage(rgbFrame.data, w, h, ch * w, QImage.Format_RGB888)

            # cria o QPixmap do QImage:
            pixmap = QPixmap.fromImage(image)

            # atualiza a label que exibira o frame do video:
            self.video.setPixmap(pixmap)
    
    # função que define o tamanho do video da webCam:
    def tamanhoWebCam(self, frame):
        width = self.video.geometry().width()
        height = self.video.geometry().height()
        resize = cv2.resize(frame, (width, height))
        return resize
