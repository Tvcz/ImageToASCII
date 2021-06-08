# ImageToASCII
An image to text converter that focuses on the accurate translation of edges and uses whitespace liberally. Proper viewing of text requires a sufficiently wide text editor with a monospaced font. Written in Python.

Feel free to submit pull requests with new features/QOL improvements. Currently I'd like to improve how it handles inputs and add options for processing gifs and videos.


<br />


### Examples:

#### Input:
![Star Destroyer](https://github.com/Tvcz/ImageToASCII/blob/main/Samples/star_destroyer.jpg?raw=true)

#### Output:
```text
             ' ~ *   .     .                ..              . *           * ..                 '      '                   . 
   `     =           .'    *'   *             `       `                   *~  -           .                ~                
* .',              .       ,                                  '      *'   ..              "   "    __                       
             ..  .~                                                       .  *           ..         "           _       *   
  ~~      o ~'    ._~   '       ~  .      ,,9>.  +___<W___,  ,=>.  "                           ~ `      `       .      _    
- ..            ,  "                       '.Y_,,____>_amg___*-M.     ~  ~ '                                =   .,    8"    
           `'.            ~    ,      _  *_-NP%WMQOMMPCMQMQQMMZMM#.       .. .   "      <o                 .  .  .      ,   
_                  `     :   `  _     .   )OQWPMPQMQ_F_KZgm%W9Q8g%.`   +~.   .        _                     ` .`            
     _     _     _     -       _         ~."''*Ppw*%QQ%WQmPP**"**.   .    #           "           ?         ,   ,   "   _.  
     "     .     "_.>    ,     *            ,..`   .___>___.   ~    *                                     <          ~+  .  
                                        _: _.:-___="**5ee_.-P~~__       ,              '                           .      .~
 "           _    _           ~   "    ^``+-.*''`~+_:a._*_P^$~Z~EP~~__     _ <-           ~              .       ` '        
             "    *'                -`. `..  `-__.__,=--*o'`"*~,_p=Gommv    '  .              _  .'      q'  *'            ~
                       ~         `._.  .        "..-*"_~_+~>*SEO6%MN~%_Z>_     .        ~~                                  
                      .`   ~   . `     -          -+-gC_:-==O%C*Z*pSMCMQaC~~__                                      _       
                           ._ -     `-        :__:EcV'HKQqQMQ&=*K9PWWE_~~M%GCS%     *             .    _       .    .      +
                     ._:- `.     -~   `-_.     pQF%%F="```.r`" .__X+#''.**"<,QS'`~~-___ ~              _.     .'            
                __--`.            -            ~'  ..'~-:2___c```..KWMQ%W%MMQQFOm**`_*."`~~_.          *'-                 .
     .>   __--`.                    `                   .~` _    . ."$'NP~PWQ*QC*_..`_.*.:,.<.  *`                  .       
        =:_.                    . -`              . ---~~``` ``  -- `-PmRc<~, ~*`q___.`_**_%.*_    ..  `       <> ~       . 
             #_,_  .         .   .`- ._.     `= . .  _`                  .*'-_. _ .?`. ._*.2O..=_      _              .   " 
             ."7*     `- ... ..   ._.::._``-- __:~.`.    `    -      ` . .  ` "^:'<`.. `~c,~._~ .%_    ..       ~'          
       .            ._. .  . `*` *~~::_::*'~-`'.`~``-+    ,    .--.``. .    . `~`.`44~Z~'.*_Q_*.z.C%.         ,          .. 
       .                   -- __ *'  ` +*``-::___~.~ **-.'. -~ .,..`__  =`  "`  .   .`-_S_+ZJ*_#q`.NE'                      
-`                               `~-   .`  . ` .*`~--`*-=._`---:.*~2_"*-:-<C--_`...` `_.*<m-o~''p,m~*F_.  #   _  +.         
                          ._.                .  ~ '-.`*`:`_.*.~-:,2J`-`' `-.~*` :-:_.* ,_`-G^q__c__a`z .>.    .   '    -_  ~
                           "'          .    .    - .~=._``.'.~.--_=--:_. *'_-`  ~=~`_.._ ~-:'-'`"^~%P#_K_*%.            .   
                                    '  .    *           ``~-:.."`"wWe``=*``--e_-*`Q%'_`:  *`      =<C>Eo___*_.       `      
                                 _        .  .        .        `-c_-     * :` =:*'`--:_':_._.-.__:---C^,_.` .h_             
                                 .       `.  "'       "      __    .`` - .. *   ',   .-=_"~~:__.  .  *~*-?~_. '>. -         
                     ~                                   ,   *'         . .  -  ...  - *UOD<_.`:.`~- __..'^."~<_.~_        >
                          .     ~                  .          .'   " =   '    '~" *`- -~~>~'"   _.*Z~`::_`~~:_.-_~Q%_.'     
                       .. *  .         _    .,     "_      <.           *     * .: -   .  `-- ..   .`    .~`- ::`~~*p_      
                        .              "            .           #.        ~ ".  .`      ` .'     ~`--_.          .`"&`      
                            " ,'                                                       .  : *           ``_`..--   -QP'     
    _.                 *   .`             .                       ~       ,               .     ~   ` "       .`*-*`j*      
    *"                     .  *       .     =   _                             _ ..     *                                    
                               .  _   .        .^                             .               _.       ..       ,_        * 
                      -  *     .`  *                   ~   *    ~-                            *'        .       "'          
```


<br />

#### Input:
![Durin's Door](https://github.com/Tvcz/ImageToASCII/blob/main/Samples/door.jpg?raw=true)

#### Output:
```text
_#=>>~>~~~~~~~+++______________________________________________________________
JL                            _.    _@W,.%QF    .                             J
JF                           _%N==cmepQgmQQmcb_QM_    .                       J
J'  _=, ,__.           .QM-aE_QXMWWC-P<C"P*MMM%RQZEm-WM.                      J
JL  %*_XL..       ____aqEWv?MP^'a%.   ___ "' ..Z'?wMSGcg%____      .m%*%.     J
JL  .'"_j        _MC_EW%p"'   .__.H8#WMMMMW8___..  ..'.WOQ%9%_     *omQ='     J
JL    qW'    . _<~8MQ"%8.___WMQQWQ%QmPqmFPmQSEQcNMWL.  .""QC6q>___            J
.L          aWM%M%W"  .%KMCE>F''.     =X%>    .`*~oMMMC.  .WQQ=S9"            J
.L         .W%PE92. _WMMcF'.         *%%QP         .*~SQM__..q$N#>%. .        J
JL      _%_Q2mM'_.6XWMF*        .__   "ZN"  __.        *-SW@9' .?QQQWQ.       J
JL      *ZPW2' *P%OKp'          QM%+ _'J.*%.>MW~         .~RNbM. *w_S%.       J
JL     .CQ=v.L__QWP'       ._L, *^*'P. J. .%***  _#_       .qN"$_..%JZO._.    J
JL   .QW"CP. .M%Q'      .  *WWZ  ~&Z._.P%__.%W> *DMM`        *Sc%_  NQQMM'    )
JL    4ZgK9 .9KO'      QWW,  .    *QW.W_JE$PJ'    "  <MM.     *OW%__*q@M%.    )
.L   JZJW'  +KW'       ~a"        .EMZZC_^PQM>       ~m^.      .pPML .QXNK    J
.L .MM''g  JMW'                     ..***``..                   *WQL  4CMWWb  J
.L  J79Q.  6SM                       .#"                         $W%.  *NWX   J
.La===+q====4~=_                     #%___,_.                   _=$=====MMQ>_.J
.T.=_       _,.*L                __=~qq~~F===___               W'.__.     __.NJ
JWwMN>_____<Md_P'                *"*M""""""M==".               *>_MNL__.._WN='J
JL  M  .... $.. _=+~=_              ***"**"*             _="`?=_ ..f .*"'. Q  J
JF _N       )F.W. 8._W.                                 .%__J' )X .j       M  J
JLP'N       .LJM  ._Q%Mmm__.                       __====SSP'  JM JF       M_ J
JW..H       .L.M,_C>"'.    *%.                   .#'      *Q%._Q' J'       %*%J
JW%.H       .$ q#Q'  W'     .L  _            _-  JL     <.  %OM'  J.       H $J
JLqQ$_       N .'K%. %M__.__0' .Q  _.    _  .6.  .Q_.   .U  #2*L  K.       Q_MJ
JL .QQS__    N J`M%%. *qR%M@_,_W"  _#    Q_  *q5___qQQXM>' JM'L6  M       _&P.J
JL .g .*mQ%__M $.%*L%>~_Q==^"`'~>=ap'_  _."q=Fe'`.**~a__.  gg.FS .N    __WPT. J
JL .F     .^QZwOL.MM"_>'        .N,__M. *a#_M         .%C>.g*W.F .L_ae%p". f. f
JF .F        $N_Q..'J'    _"      9.'.    ..L      *%   .%*QM'#_>*Q>"'     ). J
J' _k        JLN.  .g _   $_     .W        .Q_     _9.   .%...P._K'        f. J
J'#'j        .Q,6  .'#P 9,.qQ=+aHM'         .qQC=M%PJ&   P.&   J%4.        fW.f
JH$.j        .M$g  JM*  *Q. ."*".      _       ...  qN   qL%  .FWW.        )'Ff
JFKML        .$.M  .f  _ .'        ._<.Q_>_.        .M _. *M. J'MN         )M'f
JF*%_"=__     N N  .L JM.8___      _OMW$%MC_      .v=Q.9%  $` $P.N       _JMF f
J` JF"=__~=__ N N   N &QW' .M'    ~oMM~O~EWm=     $%  N_q. J. *L.j   __=C>".F )
JF )F   .*=v_?Q.N   N<Q6=_.'.      =OM%gOQQ+      ."^G=QM3.8  .&.L_=^C>"'  .L $
JL J'       *>_*Q   6J'  _M         "<'W'w.'        9L .*%"S   9P"_>".     .L $
JF J.         )K.   J' *=m'            *            *qP" .K    *,P.        .j $
JF $.         )PL   g                                     Q    JW.         .j $
J' $.         JL%  .H                                     ).  .PK          .N $
JL J.         .L$. .j                                     JL  J'N          .H $
JL $.         .LJF .f                                     JL  $.N          .N $
JL 4.         .HJ. Jj                                     .L  N.j           % $
JL P.          MJ. JF                                     JL  %.j           M f
JL E.          Q6  .L                                     J'  $U'           M $
JL N.          $"  .L                                     J`  .N.           M $
JL g           ).  .N                                     9    K.           H 9
JL H           )L   V.             ,~%:<,                .F    M            N 6
JL M           JL   .K             .%%Q#P               .W.    M            N.g
.L M           .L    .~Pb.         bQ'                ,=~'    .f            Q.g
.L6~============_L      *5.        .                 4'       #==+_________=4LK
.Mg_?~+==~=~=~~2_W.      .*=_____..             .___>'        E_'~~~====~++2_gN
.M..*'"*'``"'"`. .&          ..`"*`""""'""~"""`"*".          .$.*'*`?^*'"*'..$W
.Q>=o=>mmmmmmomoaoW=mmmmmmmmmm=mcm`===m==omo===Fmmm=ommommmmmmmmmmmmmmmmmPPPFqQ
.WMO'__.__v_ _.__.______.__._SL.__=P=J<._.___N____ _O_______#N____.._._____S,.H
.M%_QgW?S.9Q''QMNQMQM%MX.M$&aQQM%'J"QWQMQMQQFW%%UM.=QQMQMQMm=QQM=o`q=QM=q=PqP*M
.W__._____,J_._______o_____Z+NOL_OM___J___,_W_ WO%__,___,.~M%___,SE_ _M.,____.H
.kMMWQ.=qp*=mMq.qoMqp=PQ.qPg'a=PMMMM=p.PVmwP=q.q=eP>W=X?H= q='m^Z*qq_~`N$""Q^=W
.WPW'Z__,J___,___,Z__.,__,_WM____.__,_,,%b8____ Hvvv.Q*g_b<=vMS H#_%6NHLM&=Q%_H
.W'P<=="P*mSP'$^PQ=*=_.'*%qm^"***''P_Z*PPPPPPP**2"""'P~NC""'*'*'$**C'Z""?F"**.M
.%WUWH>-..L.'6QCmWH%=QcNWWP_=MM=#b.N==W>o%o%_PWMNJZH>%QmPQK%%%Me6.ZQMWWXMWMMMLN
.$`'"""*' *^'"'""'*''*'''"*'"'` *' **'*.`K_P'*'"*.`*""*'""*'"**'*'`''**_______N
```
