@namespace
class SpriteKind:
    EnemyFire = SpriteKind.create()
    Boss = SpriteKind.create()

def on_a_pressed():
    global Fire_Ball
    Fire_Ball = sprites.create_projectile_from_sprite(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . 4 4 . . . . . . . 
                    . . . . . . 4 5 5 4 . . . . . . 
                    . . . . . . 2 5 5 2 . . . . . . 
                    . . . . . . . 2 2 . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        Space_Ship,
        0,
        -150)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_on_overlap(sprite, otherSprite):
    MyEnemy.destroy(effects.confetti, 100)
    otherSprite.destroy()
    info.change_score_by(3)
sprites.on_overlap(SpriteKind.projectile, SpriteKind.Boss, on_on_overlap)

def on_on_destroyed(sprite2):
    global bossLevel
    bossLevel = 0
    info.start_countdown(30)
sprites.on_destroyed(SpriteKind.Boss, on_on_destroyed)

def on_on_overlap2(sprite3, otherSprite2):
    info.change_life_by(-1)
    otherSprite2.destroy()
sprites.on_overlap(SpriteKind.player, SpriteKind.EnemyFire, on_on_overlap2)

def on_countdown_end():
    global Boss2, bossLevel
    Boss2 = sprites.create(img("""
            . . 5 . 5 . . . . . . 5 . 5 . . 
                    . . 5 . . 7 . . . . 7 . . 5 . . 
                    . . . 7 . 7 . . . . 7 . 7 . . . 
                    . . . 7 7 7 5 5 5 5 7 7 7 . . . 
                    . . . . . 7 7 5 5 7 7 . . . . . 
                    . . . . . 7 7 7 7 7 7 . . . . . 
                    . . . . 7 7 7 7 7 7 7 7 . . . . 
                    . . . 7 7 7 1 1 1 1 7 7 7 . . . 
                    . . 7 7 7 1 1 1 1 1 1 7 7 7 . . 
                    . . . 7 1 1 1 f f 1 1 1 7 . . . 
                    . . 7 7 7 1 1 1 1 1 1 7 7 7 . . 
                    . . 7 . 7 7 1 1 1 1 7 7 . 7 . . 
                    . . . . . 7 7 7 7 7 7 . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        SpriteKind.enemy)
    Boss2.set_kind(SpriteKind.Boss)
    Boss2.set_bounce_on_wall(True)
    Boss2.set_position(76, 10)
    bossLevel = 1
    Boss2.set_velocity(70, 0)
info.on_countdown_end(on_countdown_end)

def on_on_overlap3(sprite4, otherSprite3):
    MyEnemy.destroy(effects.confetti, 100)
    otherSprite3.destroy()
    info.change_score_by(1)
sprites.on_overlap(SpriteKind.projectile, SpriteKind.enemy, on_on_overlap3)

def on_on_overlap4(sprite5, otherSprite4):
    info.change_life_by(-1)
    otherSprite4.destroy()
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_on_overlap4)

ENEMYfire: Sprite = None
Boss2: Sprite = None
bossLevel = 0
MyEnemy: Sprite = None
Fire_Ball: Sprite = None
Space_Ship: Sprite = None
scene.set_background_image(assets.image("""
    background
"""))
Space_Ship = sprites.create(img("""
        . . . . . . . 5 . . . . . . . . 
            . . . . . . 3 a 3 . . . . . . . 
            . . . . . 3 a a a 3 . . . . . . 
            . . . 3 3 a a a a a 3 3 . . . . 
            . . 3 a a a a a a a a a 3 . . . 
            . 3 3 3 3 3 3 3 3 3 3 3 3 3 . . 
            9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 . 
            5 8 8 8 8 8 8 8 8 8 8 8 8 8 5 . 
            . 5 8 5 8 5 8 5 8 5 8 5 8 5 . . 
            . . . 8 8 8 8 8 8 8 8 8 . . . . 
            . . 8 . . a a a a a . . 8 . . . 
            . . . . . . 8 a 8 . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . .
    """),
    SpriteKind.player)
controller.move_sprite(Space_Ship, 100, 100)
Space_Ship.set_position(75, 100)
Space_Ship.set_stay_in_screen(True)
info.start_countdown(30)

def on_update_interval():
    global ENEMYfire, MyEnemy
    if bossLevel:
        ENEMYfire = sprites.create_projectile_from_sprite(img("""
                . . . . . . . . . . . . . . . . 
                            . . . . . . . 2 1 2 . . . . . . 
                            . . . . . . . 2 1 2 . . . . . . 
                            . . . . . . . 2 1 2 . . . . . . 
                            . . . . . . . 3 1 3 . . . . . . 
                            . . . . . . 2 3 1 3 2 . . . . . 
                            . . . . . . 2 1 1 1 2 . . . . . 
                            . . . . . . 2 1 1 1 3 . . . . . 
                            . . . . . . 3 1 1 1 3 . . . . . 
                            . . . . . . 3 1 1 1 3 . . . . . 
                            . . . . . . 3 1 1 1 3 . . . . . 
                            . . . . . . 2 3 1 3 2 . . . . . 
                            . . . . . . . 2 2 2 . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . .
            """),
            Boss2,
            0,
            150)
        ENEMYfire.set_kind(SpriteKind.EnemyFire)
    else:
        MyEnemy = sprites.create(img("""
                ........................
                            ........................
                            ........................
                            ........................
                            ..........ffff..........
                            ........ff1111ff........
                            .......fb111111bf.......
                            .......f11111111f.......
                            ......fd11111111df......
                            ......fd11111111df......
                            ......fddd1111dddf......
                            ......fbdbfddfbdbf......
                            ......fcdcf11fcdcf......
                            .......fb111111ffff.....
                            ......fffcdb1bc111cf....
                            ....fc111cbfbf1b1b1f....
                            ....f1b1b1ffffbfbfbf....
                            ....fbfbfffffff.........
                            .........fffff..........
                            ..........fff...........
                            ........................
                            ........................
                            ........................
                            ........................
            """),
            SpriteKind.enemy)
        MyEnemy.set_position(76, -3)
        MyEnemy.set_velocity(0, 70)
        MyEnemy.x = randint(5, 155)
        animation.run_image_animation(MyEnemy,
            [img("""
                    ........................
                                ........................
                                ........................
                                ........................
                                ........................
                                ..........ffff..........
                                ........ff1111ff........
                                .......fb111111bf.......
                                .....fffc1111111f.......
                                ...fc111cd1111111f......
                                ...f1b1b1b1111dddf......
                                ...fbfbffcf11fcddf......
                                ......fcf111111bbf......
                                .......ccbdb1b1fcf......
                                .......fffbfbfdff.......
                                ........ffffffff........
                                ........fffffffffff.....
                                .........fffffc111cf....
                                .........fffff1b1b1f....
                                ..........ffffbfbfbf....
                                ...........ffff.........
                                ........................
                                ........................
                                ........................
                """),
                img("""
                    ........................
                                ........................
                                ........................
                                ........................
                                ........................
                                ..........ffff..........
                                ........ff1111ff........
                                .......fb111111bf.......
                                .......f11111111f.......
                                ......fd11111111df......
                                ....7.fd11111111df......
                                ...7..fd11111111df......
                                ...7..fd11111111df......
                                ...7..fddd1111dddff.....
                                ...77.fbdbfddfbdbfcf....
                                ...777fcdcf11fcdcfbf....
                                ....77fffbdb1bdffcf.....
                                ....fcb1bcffffff........
                                ....f1c1c1ffffff........
                                ....fdfdfdfffff.........
                                .....f.f.f..............
                                ........................
                                ........................
                                ........................
                """),
                img("""
                    ........................
                                ........................
                                ........................
                                ........................
                                ..........ffff..........
                                ........ff1111ff........
                                .......fb111111bf.......
                                .......f11111111f.......
                                ......fd111111111f......
                                ......fd11111111df......
                                ......fd11111111df......
                                ......fcdd1111ddcff.....
                                .......fbcf11fcbfbbf....
                                .......ffbdb1bdffff.....
                                ........fcbfbfdf........
                                ........ffffffff........
                                ......ffffffffff........
                                .....fcb1bcffff.........
                                ......ffbff.............
                                ........................
                                ........................
                                ........................
                                ........................
                                ........................
                """),
                img("""
                    ........................
                                ........................
                                ........................
                                ........................
                                ..........ffff..........
                                ........ff1111ff........
                                .......fb111111bf.......
                                .......f11111111f.......
                                ......fd11111111df......
                                ......fdd111111ddf......
                                ......fbdd1111dddf......
                                ......fcdbfddfbdbf......
                                .......fbcf11fcbfff.....
                                .......ffb1111bcfbcf....
                                ........fcdb1bdfbbbf....
                                .......ffffffffffcf.....
                                .....fcb1bcfffff........
                                .....f1b1b1ffff.........
                                ......ffbff.............
                                ........................
                                ........................
                                ........................
                                ........................
                                ........................
                """)],
            500,
            False)
game.on_update_interval(2000, on_update_interval)
