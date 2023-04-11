# área das importações:
from PyQt5.QtWidgets import QWidget, QLabel, QDesktopWidget
from PyQt5.QtCore import Qt
from Programacao.Back_End import Processamento

# classe da interface gráfica da aplicação:
class Interface(QWidget):
    # função de inicialização da classe:
    def __init__(self):
        super().__init__()

        # variaveis da tela:
        self.altura = 1
        self.largura = 1
        self.titulo = 'Contador de dedos'

        # variavel relativa ao back-end do programa:
        self.backEnd = ''

        self.label1 = QLabel(self)
        self.label1.setText("<u>'esc'</u> to close")
        self.label1.setStyleSheet("color: red; font-size: 18px;")
        self.label1.setAlignment(Qt.AlignHCenter)

        # chama a função que calcula e posiciona a label
        self.posicionaLabel1()

        # QLabel do video da camera:
        self.video = QLabel(self)
        self.video.setStyleSheet('background-color: black')
        self.video.move(5, 5)

        # chama a função que calcula e posiciona o video da camera:
        self.tamanhoVideo()

        # QLabel informação do que fazer:
        self.Informacao = QLabel(self)      
        self.Informacao.setText('Não está sendo detectado uma mão,\nposicione seu mão melhor na camera!')
        self.Informacao.setStyleSheet("color: black; font-size: 42px; background-color: yellow")
        self.Informacao.setAlignment(Qt.AlignHCenter)

        # chama a função que calcula e posiciona a label de informação do que fazer:
        self.posicionaInformacao()

        # QLabel de mão identificada:
        self.Identificada = QLabel(self)
        self.Identificada.setText("Mão identificada!")
        self.Identificada.setStyleSheet("color: black; font-size: 28px;")
        self.Identificada.resize(375, 35)
        self.Identificada.setAlignment(Qt.AlignHCenter)

        # chama a função que calcula e posiciona a label que diz que uma mão foi identificada:
        self.posicionaIdentificada()

        # QLabel de mão identificada:
        self.tituloQuantidade = QLabel(self)
        self.tituloQuantidade.setText("Quantidade de dedos:")
        self.tituloQuantidade.setStyleSheet("color: black; font-size: 28px;")
        self.tituloQuantidade.resize(375, 35)
        self.tituloQuantidade.setAlignment(Qt.AlignHCenter)

        # chama a função que calcula e posiciona a label de titulo da quantidade de dedos:
        self.posicionatituloQuantidade()

        # QLabel numero de dedos:
        self.numeroDedos = QLabel(self)
        self.numeroDedos.setText("05 dedos\nlevantados")
        self.numeroDedos.setStyleSheet("color: black; font-size: 28px;")
        self.numeroDedos.resize(375, 70)
        self.numeroDedos.setAlignment(Qt.AlignHCenter)

        # chama a função que calcula e posiciona a label de numero de dedos:
        self.posicionaNumeroDedos()

        # instancia a classe do backEnd na variavel:
        self.backEnd = Processamento(self, self.video, self.Informacao, self.Identificada, self.tituloQuantidade, self.numeroDedos)

        # chama a função que carrega a janela e suas propriedades:
        self.carregarJanela()

    # função que carrega a janela e suas propriedades:
    def carregarJanela(self):
        self.resize(self.largura, self.altura)
        self.setWindowTitle(self.titulo)
        self.showFullScreen()

    # função que calcula e posiciona o video da camera:
    def tamanhoVideo(self):
        # obtem a geometria da tela:
        desktopGeometry = QDesktopWidget().availableGeometry() 

        # tamanho da altura da tela:
        height = desktopGeometry.height()

        # tamanho da largura da tela:
        width = desktopGeometry.width()

        # obtem a posição relativa ao eixoX do video da camera:
        eixoX = self.video.geometry().x()

        # obtem a posição relativa ao eixoY do video da camera:
        eixoY = self.video.geometry().y()

        # calcula a altura do video:
        calcHeight = int(height - eixoY - (height * 0.15)) 

        # calcula a largura do video:
        calcWidth = int((width - eixoX) * 0.75)

        # redimensiona o video da camera:
        self.video.resize(calcWidth, calcHeight)

    # função que calcula e posiciona a label de informação do que fazer:
    def posicionaInformacao(self):
        # obtem a geometria do video:
        videoGeometry = self.video.geometry()

        # obtem o eixoX do video:
        eixoX_video = videoGeometry.x()

        # obtem o eixoY do video:
        eixoY_video = videoGeometry.y()

        # obtem a altura do video:
        height_video = videoGeometry.height()

        # obtem a largura do video:
        width_video = videoGeometry.width()

        # calcula o eixoX da informação:
        eixoY = eixoY_video + height_video + 5

        # move a informação:
        self.Informacao.move(eixoX_video, eixoY)

        # redimensiona a informação:
        self.Informacao.resize(width_video, 100)

    # função que calcula e posiciona a label1:
    def posicionaLabel1(self):
        # obtem a geometria da tela:
        desktopGeometry = QDesktopWidget().availableGeometry() 

        # tamanho da largura da tela:
        width = desktopGeometry.width()

        # tamanho da largura da label1:
        width_label1 = self.label1.geometry().width()

        # define a posição do eixoX da label1:
        eixoX = width - (width_label1 // 2)

        # define a posição do eixoY da label1:
        eixoY = 5

        # move a label1:
        self.label1.move(eixoX, eixoY)

    # função que calcula e posiciona a label que diz que uma mão foi identificada:
    def posicionaIdentificada(self):
         # obtem a geometria da tela:
        desktopGeometry = QDesktopWidget().availableGeometry() 

        # tamanho da altura da tela:
        height = desktopGeometry.height()

        # obtem a largura do video da camera:
        width_video = self.video.geometry().width()

        # obtem o eixoX do video da camera:
        eixoX_video = self.video.geometry().x()

        # define a posição do eixoX da label identificada:
        eixoX = int(width_video + eixoX_video + 15)

        # define a posição do eixoY da label identificada:
        eixoY = int(height * 0.25)

        # move a label identificada:
        self.Identificada.move(eixoX, eixoY)
    
    # função que calcula e posiciona a label de titulo da quantidade de dedos:
    def posicionatituloQuantidade(self):
        # obtem a largura do video da camera:
        width_video = self.video.geometry().width()

        # obtem o eixoX do video da camera:
        eixoX_video = self.video.geometry().x()

        # define a posição do eixoX da label  de titulo da quantidade de dedos:
        eixoX = int(width_video + eixoX_video + 15)

        # obtem o eixoY da label identificada:
        eixoY_Identifica = self.Identificada.geometry().y()

        # define a posição do eixoY da label  de titulo da quantidade de dedos:
        eixoY = eixoY_Identifica + 35

        # move a label  de titulo da quantidade de dedos:
        self.tituloQuantidade.move(eixoX, eixoY)
    
    # função que calcula e posiciona a label de numero de dedos:
    def posicionaNumeroDedos(self):
        # obtem a largura do video da camera:
        width_video = self.video.geometry().width()

        # obtem o eixoX do video da camera:
        eixoX_video = self.video.geometry().x()

        # define a posição do eixoX da label  de numero de dedo:
        eixoX = int(width_video + eixoX_video + 15)

        # obtem o eixoY da label de titulo da quantidade de dedos:
        eixoY_tituloQuantidade = self.tituloQuantidade.geometry().y()

        # define a posição do eixoY da label de numero de dedo:
        eixoY = eixoY_tituloQuantidade + 35

        # move a label  de titulo da quantidade de dedos:
        self.numeroDedos.move(eixoX, eixoY)

    # função que ve quando uma tecla é clicada:     
    def keyPressEvent(self, event):
            # verifica se a tecla clicada é o 'esc':
            if event.key() == Qt.Key_Escape:
                # fecha a tela:
                self.close()
