import pygame # pygame 라이브러리를 불러옵니다. 게임을 만들 때 필요한 도구들이 여기에 있어요.

pygame.init() # pygame을 시작합니다. 이걸로 게임을 만들 준비를 해요.

WHITE = (255,255,255) # 색깔을 저장하는 변수입니다. 여기서는 흰색을 나타내요.

size = [400,300] # 게임 화면의 크기를 저장하는 변수입니다. 너비 400, 높이 300으로 설정했어요.
screen = pygame.display.set_mode(size) # 설정한 크기의 게임 화면을 만듭니다.

done = False # 게임이 계속 실행되는지 확인하는 변수입니다. 게임이 계속되면 False, 종료하면 True로 바뀌어요.
clock = pygame.time.Clock() # 시간을 관리하는 변수입니다. 게임의 속도를 조절할 때 사용해요.

airplane = pygame.image.load('5.chap\image\plane.png') # 비행기 이미지를 불러오는 부분입니다. 이미지 파일을 사용해요.
airplane = pygame.transform.scale(airplane,(60,45)) # 불러온 이미지의 크기를 조절합니다. 비행기의 크기를 설정해요.

def runGame():
    global done, airplane # global 키워드는 전역변수를 함수 안에서 사용하겠다는 뜻입니다. 여기서는 done과 airplane 변수를 사용할 거예요.
    x = 20
    y = 24 # 비행기의 시작 위치를 x, y 변수로 설정합니다.

    while not done: # 'while not done'은 'done이 False인 동안 계속 반복'한다는 뜻입니다. 게임이 실행되는 동안 계속되요.
        clock.tick(50) # 게임의 프레임 속도를 설정합니다. 여기서는 초당 10번 화면을 갱신하도록 해요.
        screen.fill(WHITE) # 화면을 흰색으로 채웁니다. 매 프레임마다 화면을 초기화하는 역할을 해요.

        for event in pygame.event.get(): # 게임에서 발생하는 이벤트(사용자 입력 등)를 처리합니다.
            if event.type == pygame.QUIT: # 'if' 문은 조건을 확인합니다. 여기서는 게임 종료 이벤트가 발생했는지 확인해요.
                done = True # 게임을 종료하기 위해 done 변수를 True로 변경합니다.

            if event.type == pygame.KEYDOWN: # 키보드가 눌렸을 때의 이벤트를 처리합니다.
                if event.key == pygame.K_UP: # 위쪽 화살표 키가 눌렸을 때 y 좌표를 감소시켜 비행기를 위로 움직입니다.
                    y -= 10
                elif event.key == pygame.K_DOWN: # 아래쪽 화살표 키가 눌렸을 때 y 좌표를 증가시켜 비행기를 아래로 움직입니다.
                    y += 10

        screen.blit(airplane,(x,y)) # 비행기 이미지를 화면에 그립니다. x와 y 좌표에 따라 위치가 결정돼요.
        pygame.display.update() # 화면에 그려진 내용을 업데이트합니다. 변경사항을 화면에 표시해요.

runGame() # runGame 함수를 호출하여 게임을 실행합니다.

pygame.quit() # 게임이 끝나면 pygame을 종료합니다.




