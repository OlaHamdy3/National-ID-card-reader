def placeOfBirth(id):
    cairo="القاهرة"
    alex="الإسكندرية"
    ps="بورسعيد"
    sw="السويس"
    Du="دمياط"
    dac="الدقهلية"
    sha="الشرقية"
    qal="القليوبية"
    ksh="كفر الشيخ"
    ghar="الغربية"
    mno="المنوفية"
    bhe="البحيرة"
    isma="الإسماعيلية"
    giza="الجيزة"
    basw="بني سويف"
    fay="الفيوم"
    men="المنيا"
    asu="أسيوط"
    soha="سوهاج"
    qen="قنا"
    asw="أسوان"
    auxo="الأقصر"
    ba="البحر الأحمر"
    wg="الوادي الجديد"
    matr="مطروح"
    shsai="شمال سيناء"
    gasai="جنوب سيناء"
    out="خارج الجمهورية"
    govID= id[7:9]
    if(govID=="01"):
        gov=cairo
    elif(govID=="02"):
        gov=alex
    elif(govID=="03"):
        gov=ps
    elif(govID=="04"):
        gov=sw
    elif(govID=="11"):
        gov=Du
    elif(govID=="12"):
        gov=dac
    elif(govID=="13"):
        gov=sha
    elif(govID=="14"):
        gov=qal
    elif(govID=="15"):
        gov=ksh
    elif(govID=="16"):
        gov=ghar
    elif(govID=="17"):
        gov=mno
    elif(govID=="18"):
        gov=bhe
    elif(govID=="19"):
        gov=isma
    elif(govID=="21"):
        gov=giza
    elif(govID=="22"):
        gov=basw
    elif(govID=="23"):
        gov=fay
    elif(govID=="24"):
        gov=men
    elif(govID=="25"):
        gov=asu
    elif(govID=="26"):
        gov=soha
    elif(govID=="27"):
        gov=qen
    elif(govID=="28"):
        gov=asw
    elif(govID=="29"):
        gov=auxo
    elif(govID=="31"):
        gov=ba
    elif(govID=="32"):
        gov=wg
    elif(govID=="33"):
        gov=matr
    elif(govID=="34"):
        gov=shsai
    elif(govID=="35"):
        gov=gasai
    else:
        gov=out
    return gov