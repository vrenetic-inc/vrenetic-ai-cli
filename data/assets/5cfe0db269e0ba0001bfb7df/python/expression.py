#!/usr/bin/python

from math import exp


def Logistic(x) : 
   return(1/(1+exp(-x))) 

def Binary(x) : 
   if x < 0.5 : 
       return 0
   else : 
       return 1

def Probability(x) : 
   if x < 0 :
       return 0
   elif x > 1 :
       return 1
   else : 
       return x


def expression_opencl(inputs):
    raise Exception('Not implemented')


def expression(inputs): 

    if type(inputs) != list:
       print('Argument must be a list')
       exit()
    if len(inputs) != 23:
       print('Incorrect number of inputs')
       exit()
    PL=inputs[0]
    DE=inputs[1]
    US=inputs[2]
    UK=inputs[3]
    ES=inputs[4]
    IT=inputs[5]
    CH=inputs[6]
    FR=inputs[7]
    FR_1=inputs[8]
    DE_1=inputs[9]
    CH_1=inputs[10]
    UA=inputs[11]
    IT_1=inputs[12]
    PL_1=inputs[13]
    ES_1=inputs[14]
    UK_1=inputs[15]
    item_projection_type=inputs[16]
    item_publisher_is_followed=inputs[17]
    item_likes=inputs[18]
    item_views=inputs[19]
    source_type=inputs[20]
    stats_item_similar_last_minute=inputs[21]
    stats_user_feed_similar_last_hour=inputs[22]
    scaled_PL = (PL-0.263158)/0.452414
    scaled_DE = (DE-0.210526)/0.418854
    scaled_US = (US-0.263158)/0.452414
    scaled_UK = (UK-0.0526316)/0.229416
    scaled_ES = (ES-0.0526316)/0.229416
    scaled_IT = (IT-0.0526316)/0.229416
    scaled_CH = (CH-0.0526316)/0.229416
    scaled_FR = (FR-0.0526316)/0.229416
    scaled_FR_1 = (FR_1-0.0526316)/0.229416
    scaled_DE_1 = (DE_1-0.210526)/0.418854
    scaled_CH_1 = (CH_1-0.105263)/0.315302
    scaled_UA = (UA-0.157895)/0.374634
    scaled_IT_1 = (IT_1-0.157895)/0.374634
    scaled_PL_1 = (PL_1-0.0526316)/0.229416
    scaled_ES_1 = (ES_1-0.157895)/0.374634
    scaled_UK_1 = (UK_1-0.105263)/0.315302
    scaled_item_projection_type = 2*(item_projection_type-0)/(1-0)-1
    scaled_item_publisher_is_followed = (item_publisher_is_followed-0.473684)/0.512989
    scaled_item_likes = (item_likes-153)/339.674
    scaled_item_views = (item_views-1353.37)/2296.52
    scaled_source_type = (source_type-0.473684)/0.512989
    scaled_stats_item_similar_last_minute = (stats_item_similar_last_minute-10)/19.1137
    scaled_stats_user_feed_similar_last_hour = (stats_user_feed_similar_last_hour-7.94737)/18.1551
    y_1_1 = Logistic (-0.0504848+ (scaled_PL*2.24656)+ (scaled_DE*1.1185)+ (scaled_US*0.330582)+ (scaled_UK*-1.905)+ (scaled_ES*1.16893)+ (scaled_IT*1.62172)+ (scaled_CH*0.551846)+ (scaled_FR*-0.745166)+ (scaled_FR_1*-0.88284)+ (scaled_DE_1*5.17138)+ (scaled_CH_1*-2.05348)+ (scaled_UA*0.265146)+ (scaled_IT_1*0.49417)+ (scaled_PL_1*2.16904)+ (scaled_ES_1*1.83683)+ (scaled_UK_1*1.64085)+ (scaled_item_projection_type*3.16362)+ (scaled_item_publisher_is_followed*1.2524)+ (scaled_item_likes*1.05947)+ (scaled_item_views*-0.738328)+ (scaled_source_type*-1.96692)+ (scaled_stats_item_similar_last_minute*1.56543)+ (scaled_stats_user_feed_similar_last_hour*-1.25104))
    y_1_2 = Logistic (6.38254+ (scaled_PL*3.2059)+ (scaled_DE*1.02009)+ (scaled_US*1.03774)+ (scaled_UK*5.24076)+ (scaled_ES*-0.76723)+ (scaled_IT*1.70139)+ (scaled_CH*-3.0478)+ (scaled_FR*-4.80918)+ (scaled_FR_1*0.306526)+ (scaled_DE_1*1.35083)+ (scaled_CH_1*1.43661)+ (scaled_UA*-0.10182)+ (scaled_IT_1*0.483042)+ (scaled_PL_1*-0.826364)+ (scaled_ES_1*0.465964)+ (scaled_UK_1*-2.40298)+ (scaled_item_projection_type*-0.412344)+ (scaled_item_publisher_is_followed*3.58904)+ (scaled_item_likes*2.00102)+ (scaled_item_views*0.631992)+ (scaled_source_type*-0.406106)+ (scaled_stats_item_similar_last_minute*-0.39135)+ (scaled_stats_user_feed_similar_last_hour*-0.127303))
    y_1_3 = Logistic (0.0765548+ (scaled_PL*3.01458)+ (scaled_DE*-0.566932)+ (scaled_US*-1.34487)+ (scaled_UK*4.4356)+ (scaled_ES*-1.58138)+ (scaled_IT*0.756534)+ (scaled_CH*0.617432)+ (scaled_FR*1.47434)+ (scaled_FR_1*0.515494)+ (scaled_DE_1*0.806222)+ (scaled_CH_1*-0.42775)+ (scaled_UA*3.6169)+ (scaled_IT_1*-0.0388166)+ (scaled_PL_1*-0.216616)+ (scaled_ES_1*0.899744)+ (scaled_UK_1*0.261028)+ (scaled_item_projection_type*-2.32776)+ (scaled_item_publisher_is_followed*-1.73553)+ (scaled_item_likes*0.86629)+ (scaled_item_views*2.25876)+ (scaled_source_type*1.79419)+ (scaled_stats_item_similar_last_minute*-1.00327)+ (scaled_stats_user_feed_similar_last_hour*0.728126))
    y_1_4 = Logistic (-2.0004+ (scaled_PL*-1.51687)+ (scaled_DE*-0.59409)+ (scaled_US*-2.0807)+ (scaled_UK*3.44382)+ (scaled_ES*-2.55584)+ (scaled_IT*1.81689)+ (scaled_CH*0.337156)+ (scaled_FR*1.30254)+ (scaled_FR_1*0.298498)+ (scaled_DE_1*-1.66059)+ (scaled_CH_1*-1.76615)+ (scaled_UA*-1.79265)+ (scaled_IT_1*-2.10144)+ (scaled_PL_1*-0.121868)+ (scaled_ES_1*-0.460238)+ (scaled_UK_1*1.09793)+ (scaled_item_projection_type*-0.1571)+ (scaled_item_publisher_is_followed*1.40475)+ (scaled_item_likes*1.10211)+ (scaled_item_views*0.319452)+ (scaled_source_type*-0.987346)+ (scaled_stats_item_similar_last_minute*-1.35148)+ (scaled_stats_user_feed_similar_last_hour*0.305836))
    y_1_5 = Logistic (-1.16837+ (scaled_PL*1.43158)+ (scaled_DE*-1.38211)+ (scaled_US*-1.6255)+ (scaled_UK*1.30637)+ (scaled_ES*5.43148)+ (scaled_IT*-1.13662)+ (scaled_CH*-1.11218)+ (scaled_FR*-0.356984)+ (scaled_FR_1*-3.66372)+ (scaled_DE_1*1.06599)+ (scaled_CH_1*-1.4497)+ (scaled_UA*-2.2043)+ (scaled_IT_1*3.02036)+ (scaled_PL_1*0.691944)+ (scaled_ES_1*-0.228074)+ (scaled_UK_1*-1.40846)+ (scaled_item_projection_type*1.51337)+ (scaled_item_publisher_is_followed*-1.60299)+ (scaled_item_likes*1.33369)+ (scaled_item_views*0.766062)+ (scaled_source_type*2.74304)+ (scaled_stats_item_similar_last_minute*-1.53878)+ (scaled_stats_user_feed_similar_last_hour*-1.95238))
    y_2_1 = Logistic (1.46642+ (y_1_1*-1.02871)+ (y_1_2*-3.32222)+ (y_1_3*-1.08605)+ (y_1_4*0.3126)+ (y_1_5*-0.0591814))
    y_2_2 = Logistic (-1.48699+ (y_1_1*-1.28338)+ (y_1_2*1.0813)+ (y_1_3*-1.06675)+ (y_1_4*-0.381318)+ (y_1_5*-1.06258))
    y_2_3 = Logistic (-1.66588+ (y_1_1*6.75084)+ (y_1_2*4.57636)+ (y_1_3*-0.795948)+ (y_1_4*-7.34214)+ (y_1_5*-3.29448))
    y_2_4 = Logistic (0.245608+ (y_1_1*2.30366)+ (y_1_2*3.67628)+ (y_1_3*-0.246362)+ (y_1_4*-2.23514)+ (y_1_5*1.67328))
    y_3_1 = Logistic (1.83935+ (y_2_1*2.1954)+ (y_2_2*-1.62444)+ (y_2_3*-7.43252)+ (y_2_4*0.184833))
    y_3_2 = Logistic (5.59718+ (y_2_1*1.81809)+ (y_2_2*0.787018)+ (y_2_3*-8.78862)+ (y_2_4*-2.35806))
    y_3_3 = Logistic (-1.49327+ (y_2_1*3.02658)+ (y_2_2*0.254228)+ (y_2_3*-1.48027)+ (y_2_4*-0.729176))
    y_3_4 = Logistic (-0.394864+ (y_2_1*-0.444262)+ (y_2_2*2.58366)+ (y_2_3*-0.365622)+ (y_2_4*1.98556))
    y_3_5 = Logistic (-2.13238+ (y_2_1*0.088487)+ (y_2_2*1.10117)+ (y_2_3*7.5479)+ (y_2_4*0.272166))
    y_3_6 = Logistic (-3.41238+ (y_2_1*-0.160183)+ (y_2_2*-2.42276)+ (y_2_3*-1.12705)+ (y_2_4*0.36958))
    y_3_7 = Logistic (-3.9379+ (y_2_1*-4.76202)+ (y_2_2*-0.29344)+ (y_2_3*7.77222)+ (y_2_4*2.6012))
    non_probabilistic_conversion = Logistic (-0.822244+ (y_3_1*-9.08942)+ (y_3_2*-6.04938)+ (y_3_3*-2.43876)+ (y_3_4*0.256248)+ (y_3_5*7.56854)+ (y_3_6*1.13401)+ (y_3_7*7.42522))
    conversion = Probability(non_probabilistic_conversion)
    
    return {
        "relevancy-index": conversion
    }

