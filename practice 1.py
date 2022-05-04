import random
import time



Player_Count = input( '請輸入玩家人數: ' )

Player_Id = [ [i+1] for i in range( 0,int( Player_Count )) ]

Player_InputChips = int(input( '請輸入所有玩家本局遊戲之籌碼: ' ))

Player_BasingPrize = int(input( '請輸入本局遊戲底檯金額: ' ))

PrizePool = int(Player_BasingPrize * len( Player_Id ))

[ i.append(Player_InputChips) for i in Player_Id ]

endline = [1,1]


while PrizePool > 0 and endline[1] > 0 :
    
    for i in Player_Id:
        
        if PrizePool > 0 and endline[1] <= 0:
            print('遊戲結束!')
            break
        
        time.sleep(1)
        TakeRange = [ random.randint( 1,13 ), random.randint( 1,13 ) ]
        TakeRange_High = max( TakeRange )
        TakeRange_Low = min( TakeRange )
        i[1] -= Player_BasingPrize
        
        print( '-------------------------------' )
        print( '' )
        print( '玩家', i[0], '號現有籌碼: ', i[1] ,'點' )
        print( '你的兩張牌是: ',TakeRange_High,TakeRange_Low )
        print( '本局遊戲獎金池現有', PrizePool ,'點')
        print( '' )
        print( '-------------------------------' )
        pdc = input('請輸入 D ( 抽牌 )/ P ( 跳過 ) 決定是否繼續: ')
        
        
        if pdc == 'D':
    
            call = int(input('若要增注，請輸入數字(若無則輸入 0 ): '))
    
            Player_Draw = random.randint( 1,13 )
    
            if TakeRange_Low < Player_Draw < TakeRange_High:
                WinPrize = Player_BasingPrize + call
                i[1] += WinPrize
                PrizePool -= WinPrize
                print( '-------------------------------' )
                print( '' )
                print( '玩家 ',i[0],' 抽到 ',Player_Draw,', 射龍門成功 ! 獲得 ',WinPrize,' 點 , 現有', i[1],' 點 !' )
                print( '本局遊戲獎金池現有', PrizePool ,'點')
                print( '' )
                print( '-------------------------------' )
    
            elif Player_Draw == TakeRange_Low or Player_Draw == TakeRange_High:
    
                LosePrize = ( Player_BasingPrize + call ) * 3
                i[1] -= LosePrize
                PrizePool += LosePrize
                print( '-------------------------------' )
                print( '' )
                print( '玩家 ',i[0],' 抽到 ',Player_Draw,' 撞柱 ! 失去 ',LosePrize,' 點 , 現有', i[1],' 點 !' )
                print( '本局遊戲獎金池現有', PrizePool ,'點')
                print( '' )
                print( '-------------------------------' )

    
            elif Player_Draw < TakeRange_Low or Player_Draw > TakeRange_High:
                
                LosePrize = ( Player_BasingPrize + call ) 
                i[1] -= LosePrize
                PrizePool += LosePrize
                print( '-------------------------------' )
                print( '' )
                print( '玩家 ',i[0],' 抽到 ',Player_Draw,' 射空 ! 失去 ',LosePrize,' 點 , 現有', i[1],' 點 !' )
                print( '本局遊戲獎金池現有', PrizePool ,'點')
                print( '' )
                print( '-------------------------------' )
            
                    
        elif pdc == 'P':
    
            LosePrize = Player_BasingPrize
            i[1] -= LosePrize
            
            

            
        PrizePool += Player_BasingPrize * len( Player_Id )
        endline = i


# 未處理 input 限制 及 錯誤警告