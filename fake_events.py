import random
def rnd(seed):
    if seed:
        r= seed/100.0 + 10* random.random()
    else:
        r= 10* random.random()
    return round(r,2)
    
for i in range(0,250):
    ev = i % 4 + 1
    tm = rnd(i)
    print 'tl.insert(TweenLite.to("#event%(ev)s", 0, {scale:1,top:%(x)s,left:%(y)s,autoAlpha:0}),%(tm)s)' % {'ev':ev,'x':int(rnd(0)*60),'y':int(rnd(0)*50),'tm':tm-0.01} 
    
    print 'tl.insert(TweenLite.to("#event%(ev)s", .5, {autoAlpha:1, delay:0,scale:%(scale)s}),%(tm)s)' % {'ev':ev,'scale':rnd(0),'tm':tm},
    print '.to("#event%(ev)s", 0.5, {autoAlpha:0},%(td)s);' % {'ev':ev,'td':tm+2}