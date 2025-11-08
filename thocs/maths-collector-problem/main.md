Coupon's Collector Problem Analysis
=================================================
> In this post I will add some comments to the Coupon collector problem solution that can help the beginner reader to understand how _Sheldon Ross_ in his _A First Course of Probability_ derives probability distribution.

Problem statement
=================================================


The key to understand the model
=================================================
The key to understand the formula is to think that the set Ai such that no i element happens among the first n look like this when i = 1 and n = 5 (intents) and N = 3 (types)

  22222
  22223
  22232
  22233
  22322
  22323
  22332
  ...
  33333
  
after having the other sets, i.e. A2 and A3, then you need to think in the following idea to understand. Also it is important to be clear what is an _Event_. An _Event_ is a subsent, not and instance of experiment occurence (element)! Then now think that you have the following _Event_

  A1 U A2 U A3 = A

In the next attempt _n + 1_ you could win or not. If you do not win, then you could win in the _n + 2_ attemp. If you do not win, you could win in the _n + 3_ attempt and so on. 

This means that your event A (union all), apart to mean thoose events were you lost just only for one coupon also means that beggining from attempt _n + 1_ you will have the chance to win!

In other words, the event _A_ means that you will won in the attemps greater than _n_.
