from gamelib import*

game=Game(1000,800, "M&Ms vs Skittles")
mms= Image("images\\mms3.jpg", game)
bk= Image("images\\background.jpg", game)
guns= Image("images\\guns.png", game)
skittles=Image ("images\\skittles.jpg", game)

starwars= Sound("Sound\\starwars.wav",1)
gun= Sound("Sound\\Gun.wav",2)
arcade= Sound("Sound\\Arcade Explo A.wav", 3)

guns.resizeTo(200,200)
skittles.resizeTo(150,150)
skittles.moveTo(150,150)


mms.resizeTo(150,150)
mms.setSpeed(6,60)
skittles.setSpeed(5,30)


while not game.over:
    game.processInput()
    bk.draw()
    starwars.play()
    mms.move("True")
    skittles.move("False")
  
    guns.moveTo(mouse.x, mouse.y)  
    
    if mms.collidedWith(mouse) and mouse.LeftButton:
        game.score+=1
        x = randint(150,650)
        y = randint(150,450)
        mms.moveTo(x,y)
        mms.speed+=2
        mms.resizeBy(-2)
        gun.play()

    if skittles.health<10:
        game.drawText("You lose!",300,0)
        game.over=True

     

    if mms.collidedWith(skittles):
        skittles.health-=1
        skittles.resizeBy(-2)
        arcade.play()

    if mms.collidedWith(mouse) and mouse.LeftButton:
       mms.health-=1
       mms.resizeBy(-2)
       arcade.play()
        
    if game.score>=30:
        game.drawText("You win!",300,0)
        game.over=True
   
   
    game.drawText("Health =  " + str(mms.health),500,0)
    game.displayScore()
    game.update(20)
game.wait(K_SPACE)
game.quit()
   


 
   
    


   




    






   




    





