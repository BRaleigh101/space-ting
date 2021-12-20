namespace SpriteKind {
    export const EnemyFire = SpriteKind.create()
    export const Boss = SpriteKind.create()
}
sprites.onCreated(SpriteKind.Enemy, function (sprite) {
	
})
controller.A.onEvent(ControllerButtonEvent.Pressed, function () {
    Fire_Ball = sprites.createProjectileFromSprite(img`
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
        `, Space_Ship, 0, -150)
})
sprites.onOverlap(SpriteKind.Projectile, SpriteKind.Boss, function (sprite, otherSprite) {
    MyEnemy.destroy(effects.confetti, 100)
    otherSprite.destroy()
    info.changeScoreBy(3)
})
sprites.onDestroyed(SpriteKind.Boss, function (sprite) {
    bossLevel = 0
    info.startCountdown(25)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.EnemyFire, function (sprite, otherSprite) {
    info.changeLifeBy(-1)
    otherSprite.destroy()
})
info.onCountdownEnd(function () {
    Boss = sprites.create(img`
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
        `, SpriteKind.Enemy)
    Boss.setKind(SpriteKind.Boss)
    Boss.setBounceOnWall(true)
    Boss.setPosition(76, 10)
    bossLevel = 1
    Boss.setVelocity(70, 0)
})
sprites.onOverlap(SpriteKind.Projectile, SpriteKind.Enemy, function (sprite, otherSprite) {
    MyEnemy.destroy(effects.confetti, 100)
    otherSprite.destroy()
    info.changeScoreBy(1)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Enemy, function (sprite, otherSprite) {
    info.changeLifeBy(-1)
    otherSprite.destroy()
})
let ENEMYfire: Sprite = null
let Boss: Sprite = null
let bossLevel = 0
let MyEnemy: Sprite = null
let Fire_Ball: Sprite = null
let Space_Ship: Sprite = null
scene.setBackgroundImage(assets.image`background`)
Space_Ship = sprites.create(img`
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
    `, SpriteKind.Player)
controller.moveSprite(Space_Ship)
Space_Ship.setPosition(75, 100)
Space_Ship.setStayInScreen(true)
info.startCountdown(25)
game.onUpdateInterval(2000, function () {
    if (bossLevel) {
        ENEMYfire = sprites.createProjectileFromSprite(img`
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
            `, Boss, 0, 150)
        ENEMYfire.setKind(SpriteKind.EnemyFire)
    } else {
        MyEnemy = sprites.create(img`
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
            `, SpriteKind.Enemy)
        MyEnemy.setPosition(76, -3)
        MyEnemy.setVelocity(0, 70)
        MyEnemy.x = randint(5, 155)
        animation.runImageAnimation(
        MyEnemy,
        [img`
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
            `,img`
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
            `,img`
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
            `,img`
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
            `],
        500,
        false
        )
    }
})