import os  
from time import time
import binascii
import math
import os.path
long_1=0
name=""
add_bits=""



#@Author Jurijus Pacalovas
class compression:
        def cryptograpy_compression4(self):
              
               


               

                def Count_adds(M1,En,En1,En3):
                        
                        En3+=1
                      
                        if En3==(8192*4)-1:
                            En3=0
                        if M1==0:
                                En-=1
                                                                             
                                                                            
                        if En==3 or M1==1:
                                En+=1
                                M1=1
                                                                                      
                        if En==(8192*4)-1:                                                                    
                                
                                M1=0
                                En=255
                        
                                
                        return M1,En,En1,En3
                

             
             
                import re                    
               
                                
                def find_smallest_longl_F_values(input_string):
                    # Extract all 'En', 'En2', 'En3', and 'Longl_F' values
                    pattern = r'En=(\d+), Longl_F=(\d+)'
                    matches = re.findall(pattern, input_string)
                
                    # Convert the extracted strings to tuples of integers
                    longl_F_values = [(int(en), int(longl_f)) for en, longl_f in matches]
                
                    if longl_F_values:
                        # Find the smallest 'Longl_F' value and its corresponding variables
                        smallest_longl_F_values = min(longl_F_values, key=lambda x: x[1])
                        return smallest_longl_F_values
                    else:
                        return None
  







                  
                
  
                

                                     
                  
                                                                      
                                   
                        

                self.name = "Written: Jurijus pacalovas"
                N5=1
                if N5==1:

                
                
                
                    Clear=""
                    name = input("What is name of file input? ")
                    long_21=len(name)
                    name_f=name[long_21-2:]
                    if name_f==".b":
                        
                            i=2
                            
                    else:
                      
                        i=1
                    #print(i)

 
    
                 
               
                       

                    
                
                    
                    
        
                    
                    if os.path.exists(name):
                            print('Path is exists!')
                    else:
                            print('Path is not exists!')
                            raise SystemExit
                    x=0
                    C1=1
                    x1=0
                    x2=0
                    x3=0
                    X2=0
                    C1=0
                    C2=0
                    C3=0
                    C4=0
                    Cot=0
                    Cot2=1
                    Cot3=0
                    
                    x = time()
                    File_information6_Times2_1=0
                    name_2=name
                    Long_Change=len(name_2)
                    compress_or_not_compress=1
                    File_information6_Times3=0
                    if i==2:
                        C=1
                    Long_Change=len(name_2)
                    s=""
                    File_information5=""
                    File_information5_2=""
                    Clear=""
                    Translate_info_Decimal=""
                    D=0
                    long_name=len(name)
           
                    with open(name, "rb") as binary_file:
                        data = binary_file.read()

                        s=str(data)
                        long_11=len(data)
                        long_17=len(data)
                        if long_17==0:
                        	 raise SystemExit
                        END_working=0
                        File_information6_Times2=0
                        File_information5_23=""
                        INFO18=""
                        File_information5_29=""
                        SpinS=0
                        while END_working<10:
                            File_information6_Times3=File_information6_Times3+1
                            D=1
                            if D==1:
                                if File_information6_Times3==1:
                                    INFO=bin(int(binascii.hexlify(data),16))[2:]#data to binary
                                    long_1=len(INFO)
                                    long_11=len(data)
                                    count_bits=(long_11*8)-long_1
                                    z=0
                                    if count_bits!=0:
                                        while z<count_bits:
                                            INFO="0"+INFO
                                            z=z+1
                                    if File_information6_Times3==1:
                                        File_information5_2=INFO
                                    n = int(File_information5_2, 2)
                                    width_bits=len(File_information5_2)
                                    width_bits=(width_bits/8)*2
                                    width_bits=str(width_bits)
                                    width_bits="%0"+width_bits+"x"
                                    width_bits3=binascii.unhexlify(width_bits % n)                                    
                                    width_bits2=len(width_bits3)
                                    data=width_bits3
                                    long_15=len(data)
                                    INFO=bin(int(binascii.hexlify(data),16))[2:]
                                    long_1=len(INFO)
                                    long_11=len(data)
                                    count_bits=(long_11*8)-long_1
                                    z=0
                                    if count_bits!=0:
                                        while z<count_bits:
                                            INFO="0"+INFO
                                            z=z+1
                                    File_information5_2=INFO
                                    Extact=File_information5_2
                                    A=int(Extact,2)                                    
                                
                                        
                                    long_13=len(File_information5_2)
                                long_12=len(File_information5_2)
                                if i==1:
                                    if long_17>(2**28)-1 and i==1:
                                        print("print file is too big!")
                                        raise SystemExit

                                if i==1:
                                   

                                             
                                                Ex=1
                                                if Ex==1:
                                                
                                                
                                                    Extract1=0
                                                    
                                                    Find=0
                                                    En=6
                                                    Ci=1
                                                    M1=0
                                                    En1=0
                                                    input_string=""
                                                    C1=""
                                                    En3=0
                                                    I8=INFO
                                                    W3=""
                                                    W4=""
                                                    block=0
                                                    IF1=""
                                                    long_F=len(I8)
                                                    #print(long_F)
                                                    FC=0
                                                    IF2=""
                                                    Z7=0
                                                    if Cot==0:
                                                        SINFO=""
                                                        Z4=INFO
                                                    if Cot==0:
                                                        SINFO=INFO
                                                    

                                                    while block<long_F:
                                                                                                                                                         IF=I8[block:block+8]
                                                                                                                                                         if FC==0:
                                                                                                                                                             IF1=I8[block+8:block+16]
                                                                                                                                                         W4+=IF
                                                                                                                                                         block+=8                                                                                             
                                                                                                                                                      
                                                                                                                                                         
                                                                                                 
                                                                                      
                                                                                                                                                         if IF1==IF:
                                                                                                                                                             
                                                                                                                                                       
                                                                                                                                                       
                                                                                                                                                             #print(IF1)
                                                                                                                                                             #print(IF2)
                                                                                                                                                             FC+=1
                                                                                                                                                             #print(FC)
                                                                                                                                                             if FC==1:
                                                                                                                                                                 
                                                                                                                                                                 W=block-8
                                                                                                 
                                                                                                                                                                 
                                                                                                                                                                 
                                                                                                                                                             
                                                          
                                                                                                                                                         if IF1!=IF:
                                                                                                                                                               
                                                                                                                                                                 if FC<4:
                                                                                                                                                                     FC=0
                                                                                                                                                                 if Z7==0:
                                                                                                                                                                    if FC<=255 and FC>=4 and len(bin(W)[2:])<16 or FC<=256*2-1 and FC>=5 and len(bin(W)[2:])<24 or FC<=256*3-1 and FC>=6  or FC<=256*3-1 and FC>=7 or  FC<=256*4-1 and FC>=8 or FC<=256*4-1 and FC>=9 or FC<=256*5-1 and FC>=10:
                                                                                                                                                                    
                                                                                                                                                                    
                                                                                                                                                                     Z7=1
                                                                                                                                                                     W1=block-16
    
                                                                                                                                                                     Sw1=format(W,'01b')
                                                                                                                                                                     Sw3=format(len(Sw1),'05b')
                                                                                                                                                                     #print(FC)
                                                                                                                                                                     
                                                                                                                                                                     Sw2=format(FC,'01b')
                                                                                                                                                                     Sw4=format(len(Sw2),'05b')
                                                                                                                                                                     W3+="0"+IF1+Sw3+Sw1+Sw4+Sw2
                                                                                                                                                                     W4=W4[:W]+W4[W1:]
                                                                                                                                                                     FC=0
                                                                                                                                                                     
                                                                                                                                                     
                                                                                                                                                                                                                                                                             
                                                                                                                                                                                                                                                                                                                                                        
                                                    W5=W3+"1"

                                                    W4=W5+W4
                                                    INFO=W4
                                                    #print(len(INFO))

                                                    while Find!=1:
                                                                        #print(Find)
                        
                                                                        Z4=""
                                                                        N3=0                                                                    
                                                                        long_F=len(INFO)
                                                                        block=0
                                                                        FC=0
                                                                        IF1=""
                                                           
                                                                        while block<long_F:
                                                                            INFO_A=INFO[block:block+En]
                                                                            
                                                                    
                                                                            longl=len(INFO_A)
                                                                            
                                                                            Counts=int(INFO_A,2)
                                                                            C=format(Counts,'01b')
                                                                            C3=En-len(C)
                                                                            #print(C1)
                                                                            if C3>=3+3 and En<=7 or C3>=4+3 and En<=15 or C3>=5+3 and En<=31 or C3>=6 +3 and En<=63 or C3>=7+3 and En<=127 or C3>=8+3 and En<=255 or C3>=9+3 and En<=511 or C3>=10+3 and En<=1023 or C3>=11+3 and En<=2047 or C3>=12+3 and En<=4095 or C3>=13+3 and En<=8191 or C3>=14+3 and  En<=(8192*2)-1 or C3>=15+3 and En<=(8192*4)-1 or INFO_A[:3]=="011" or INFO_A[:3]=="010":
                                                                               
        
                                                                                    #print(C3)
                                                                                    
                                                                                    
                                                                                    
                                                                                    
                                                                                    
                                                                                    
                                                                         
        
                                                                                          
                                                                                
                                                                              
                                                                                 
        
                                                                                  
                                                                                 
                                                                                    
                                                                                Counts=int(INFO_A,2)
                                                                                C=format(Counts,'01b')
                                                                                C4=En-len(C)
                                                                                
                                                                                
                                                                                                                                                                 
                                                                                if En<=7:
                                                                                    C1=format(C4,'03b')                                                                                             
                                                                                elif En<=15:
                                                                                    C1=format(C4,'04b')
                                                                                    
                                                                                    
                                                                                elif En<=31:
                                                                                    C1=format(C4,'05b')
                                                                                    
                                                                                elif En<=63:
                                                                                    C1=format(C4,'06b')                                                                           
                                                                                elif En<=127:
                                                                                    C1=format(C4,'07b')                                                                                                                                                                     
    
                                                                                elif En<=255:
                                                                                    C1=format(C4,'08b') 
                                                                                    
                                                                                elif En<=511:
                                                                                    C1=format(C4,'09b')                                                                                                         
                                                                                    
                                                                                elif En<=1023:
                                                                                    C1=format(C4,'010b')   
                                                                                    
                                                                                elif En<=2047:
                                                                                    C1=format(C4,'011b')  
                                                                                    
                                                                                elif En<=4095:
                                                                                    C1=format(C4,'012b')                                                                                                                                                                                                                                                                        
                                                                                elif En<=8191:
                                                                                    C1=format(C4,'013b') 
                                                                                    
                                                                                elif En<=(8192*2)-1:
                                                                                    C1=format(C4,'014b')                                                                                                      
                                                                                elif En<=(8192*4)-1:
                                                                                    C1=format(C4,'015b')  
                                                                                    
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          
                                                                                C2=format(longl,'06b') 
                                                                                                                                                            
        
                                                                                                                                                                                                
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
                                                                                       
                                                                                       
                                                                                if C3!=1:
                                                                                       Z5="011"+C1+C
    
                                                                                       #print(Z5) 
                                                                                           
                                                                                       
                                                                                if C3==1:
                                                                                       Z5="010"+INFO_A[2:]
                                                                                       #print(Z5)
                                                                                       
                                                                                       
                                                                                       
                                                                                                                                                                                                                                       #print(INFO_A)
                                                                                   #print(C1)
                                                                                   #print(INFO_A)
                                                                            else:
                                                                            
                                                                                   Z5=INFO_A
                                                                                   
                                                                                   #not six zeros else 7 zeros or more left or 2-5 zeros
                                                                            
                        
                                                                            
                                                                                 #change back
                                                                                
                                                                         
                                                                                #same size
                                                                                
                        
                                                                           
                                                                            Z4+=Z5
                                                                            #print(Find)
                                                                            block+=En
                                                                            
                                                                   
    
                                                                        if  Find==2 or En3==(8192*4)-2:
                                                                                    Find=1
                                                                                    Extract1=1                                                             
                                                                                                   
                                                                        
                                                                        elif En3==(8192*4)-3 and Find==3:
                                                                            smallest_longl_F_values = find_smallest_longl_F_values(input_string)
                                                                            
                                                                            if smallest_longl_F_values:
                                                                                en, longl_F = smallest_longl_F_values
                                                                                En=int(en)
                                                                                
                                                                                Find=2     
                                                                                                                    
                                                                                                                                                                                                                                                                                                                                                                                    
                                                                                                                                                                                                                                                                                                                                                                                
                                                                                                                                                                                                                                                                                                                                                                                
                                                                                                                                                                                                                                                                                                                                                                                
                                                                                                                                                                                                                                                                                                                                                                                
                                                                                                                                                                                                                
                                                                                                                                                                                                                                                                                                                                                                                    
                                                                                                                                                                                                                                                                                                                                                                                    
                                                                        elif len(Z4)+8+13+8+len(C1) < long_11*8 and len(C1)!=0:
                                                                            
                                                                            
                                                                            input_string+= "En="+str(En)+", "+"Longl_F="+str(len(Z4))+" / "
                                                                       
                                                                            
                                                                        
                                                                            
                                                                            
                                                                            
                                                                            if len(input_string)>100:
                                                                             smallest_longl_F_values = find_smallest_longl_F_values(input_string)
                                                                             if smallest_longl_F_values:
                                                                                 en, longl_F = smallest_longl_F_values
                                                                                 input_string= "En="+str(en)+", "+"Longl_F="+str(longl_F)+" / "
                                                                                 #print(input_string)
                                                                                 
                                                                                                                                                                                                                                                                                           
                                                                                                                                                                                                                                                                                           
    
                                                                            Find=3
                                                                            M1,En,En1,En3=Count_adds(M1,En,En1,En3)
                                                                            
                                                                            
                                                                                 #print(En)
                                                                                 #print(len(Z4))   
                                                                                 
                                                                        else:
                                                                                 M1,En,En1,En3=Count_adds(M1,En,En1,En3)
                                                                                 
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
                                                    if Ci==1:               
                                                                
                                                               
                                                                    N3=1
                                                                                                                     
                                                                    
    
                                                                    W="0"+str(len(C1))+"b"
                                                                    CL1=format(longl,W)        
                                                                    CL2=format(En,'015b')
                                                                
                                                                    
                                                                 
                                                                   
                                                                    #print(N3)
                                                                                                                             
                                                                    if N3==1:
    
                                                                         
                                                                         
                                                                           
                                                                         
                                                                           #print(Long_PM1)
                                                                           N3=1
                                                                           Cot+=1
                                                                           #print(Cot)
                                                                           #print(len(Z4))
                                                                           #print(long_11)
                                                                           INFO=CL2+CL1+Z4
                                                                        
                                                                           
                                                                           if Cot==1:
                                                                                                                                                                            Cot2=Cot
                                                                                                                                                                            long_11=long_11*8

                                                                               

                                                                               
                                                                           
                                                                           
                                                                           Extract1=0
                                                                           if len(Z4)<=long_11 or Cot==255:
                                                                               long_11=len(Z4)
                                                                            
                                                                               INFOS=INFO
                                                                             
                                                                          
                                                                               Cot2=Cot
                                                                               
                                                                           if len(Z4)>long_11 or Cot>Cot2+1 or Cot==255:
                                                                                                                 
                                                                                                                 
                                                                               N3=2
                                                                               
                                                                               Extract1=1
                                                                               
                                                                                                                                                    
                                                                           if N3==2:
                                                                               Scot=format(Cot2,'08b')
                                                                               if Cot==1:
                                                                                   File_information5_17="1"+Scot+INFO
                                                                                   
                                                                                   
                                                                               if Cot!=1:
                                                                                   File_information5_17="1"+Scot+INFOS                                                                                 
                                                                               N4=2
                                                                               if N4==2:                                                                             
                                                                                    
                                                                                       long_1=len(File_information5_17)
                                                                                       add_bits=""
                                                                                       count_bits=8-long_1%8
                                                                                       z=0
                                                                                       if count_bits!=0:
                                                                                               while z<count_bits:
                                                                                                       add_bits="0"+add_bits
                                                                                                       z=z+1
                                                                                       File_information5_17=add_bits+File_information5_17                                                                                     

                                                                             
                                                                               
                                                    if Extract1==1:                
                                                            L=len(File_information5_17)
                                                            #print(L)
                                                            n = int(File_information5_17, 2)
                                                            width_bits=len(File_information5_17)
                                                            width_bits=(width_bits//8)*2
                                                            width_bits=str(width_bits)
                                                            width_bits="%0"+width_bits+"x"
                                                            width_bits3=binascii.unhexlify(width_bits % n)
                                                            width_bits2=len(width_bits3)
                                                            File_information5_2=Clear
                                                        
                                                            jl=width_bits3
                                                            name1=name+".b"

                                                   
                                                    
                                                            with open(name1, "wb") as f2:
                                                                f2.write(jl)
                                                            
                                                            x2 = time()
                                                            x3=x2-x
                                                            xs=float(x3)
                                                            xs=str(xs)
                                                            return xs;
                         


                                if i==2:
                                    if C==1:
                                        Extract1=0
                                        if   File_information6_Times2==0:

      
                                            
                                          
                                                        File_information5=INFO    
                                                        if   Cot3==0:
                                                                long_16=len(File_information5)
                
                                                                if File_information5[:1]=="0":
                                                                    while File_information5[:1]!="1":
                                                                        if File_information5[:1]=="0":
                                                                            File_information5=File_information5[1:]
                                                                            
                                                                            
                                                                if File_information5[:1]=="1":
                                                                    File_information5=File_information5[1:]
                                                        INFO=File_information5         
                                                        if   Cot3==0:                
                                                    
                                                                    Cot4=int(INFO[:8],2)
                                                                    #print(Cot4)
                                                                    INFO=INFO[8:]
                                                                    
                                                                    
                                                                    
                                                        while Extract1!=1:
                                                                
                                                                
                                                                    
                                                                En=int(INFO[:15],2)
                                                                    #print(longl)
                                                                INFO=INFO[15:]
                                                                En2=0
                                                                
                                                                if En<=7:
                                                                    longl=int(INFO[:3],2)
                                                                    #print(longl)
                                                                    INFO=INFO[3:]
                                                                    SEN=3  
                                                                
                                                                if En<=15:
                                                                    longl=int(INFO[:4],2)
                                                                    #print(longl)
                                                                    INFO=INFO[4:]
                                                                    SEN=4     
                                                                
                                                                elif En<=31:
                                                                    longl=int(INFO[:5],2)
                                                                    #print(longl)
                                                                    INFO=INFO[5:]
                                                                    SEN=5                                  
                                                                elif En<=63:
                                                                    longl=int(INFO[:6],2)
                                                                    INFO=INFO[6:]
                                                                    SEN=6 
                                                                    
                                                                elif En<=127:
                                                                    longl=int(INFO[:7],2)
                                                                    INFO=INFO[7:]
                                                                    SEN=7                                       
                                                                                                                                              
                                                                elif En<=255:
                                                                    longl=int(INFO[:8],2) 
                                                                    INFO=INFO[8:]  
                                                                    SEN=8                                      
                                                                                                            
                                                                                                                                                                                            
                                                                elif En<=511:
                                                                    longl=int(INFO[:9],2) 
                                                                    INFO=INFO[9:]
                                                                    SEN=9                                       
                                                                elif En<=1023:
                                                                    longl=int(INFO[:10],2) 
                                                                    INFO=INFO[10:]
                                                                    SEN=10                                                                                                                            
                                                                elif En<=2047:
                                                                    longl=int(INFO[:11],2) 
                                                                    INFO=INFO[11:]
                                                                    SEN=11                     
                                 
                                                                elif En<=4095:
                                                                    longl=int(INFO[:12],2) 
                                                                    INFO=INFO[12:]
                                                                    SEN=12
                                                                    
                                                                    
                                                                elif En<=8191:
                                                                    longl=int(INFO[:13],2) 
                                                                    INFO=INFO[13:]
                                                                    SEN=13                                                                                   
                                                                elif En<=(8192*2)-1:
                                                                    longl=int(INFO[:14],2) 
                                                                    INFO=INFO[14:]
                                                                    SEN=14                                                                                                                                                                       
                                                                elif En<=(8192*4)-1:
                                                                    longl=int(INFO[:15],2) 
                                                                    INFO=INFO[15:]
                                                                    SEN=15                                   
                                                                           
                                                                
                                                                Extract1=0
                            
                                                                Z4=""
                                                                N3=0
                                                                long_F=len(INFO)
                                                                block=0
                                                                Save=0
                                                                           
                                                                while Save!=1:
                                                                                              if Save==0:
                                                                                                    C9=0
                                                                                                  
                                                                                                
                                                                                                    O=INFO[block:block+3]
                                                                                                    
                                                                                                    
                                                                                                    
                                                                                                    if O=="010":
                                                                                               
                                                                                                           block+=3
                                                                                                           OC=INFO[block:block+En-2]
                                                                                                           E=int(OC,2)
                                                                                                           En1="0"+str(En-2)+"b"
                                                                                                           
                                                                                                           ZE=format(E,En1)
                                                                                                           C="0"+str(longl-2)+"b"
                                                                                                           ZE=format(E,En1)
                                                                                                           Z2Z=format(E,C)
                                                                                                           ZE="01"+ZE
                                                                                                           Z2Z="01"+Z2Z
                                                                                                           block+=En-2                                                                                   
                                        
                                                                                                             
                                                                                                        
                                                                                                        
                                                                                                        
                                                                                                                                            
                                                                                                    
                                                                                                    elif O=="011":
                                                                                               
                                                                                               
                                                                                                        block+=3
                                                                                                        
                                                                                                        if En<=(8192*4)-1:                                                      
                                                                                                        
                                                                                                            OCl=INFO[block:block+SEN]
                                                                                                            Size=int(OCl,2)
                                                                                                            block+=SEN                                                               
                                        
                                        
                                                                                                           
                                                                                                        EB=INFO[block:block+(En-Size)]
                                                                                                        S=len(EB)
                                                                                                       
                                                                                                        block+=En-Size
                                                                                                        En1="0"+str(En)+"b"
                                                                                                        if S>0:
                                                                                                            E=int(EB,2)
                                                                                                        else:
                                                                                                            E=0
                                                                                                        ZE=format(E,En1)
                                                                                                        C="0"+str(longl)+"b"
                                                                                                        ZE=format(E,En1)
                                                                                                        Z2Z=format(E,C)
                                        
                                                                                                                 
                                                                                                                    
                                                                                                    else:
                                                                                                           EB=INFO[block:block+En]
                                                                                                           block+=En
                                                                                                           En1="0"+str(En)+"b"
                                                                                                          
                                        
                                                                                                           E=int(EB,2)
                                                                                                           ZE=format(E,En1)
                                                                                                           C="0"+str(longl)+"b"
                                                                                                           ZE=format(E,En1)
                                                                                                           Z2Z=format(E,C)                                                                                                   
                                            
                                                                                                    
                                                                                                                                                    
                                                                                                 
                                                                                            
                                                                                                    Z2=ZE
                                                                                                    #print(Z2)
                                        
                                                                                                    Z4+=Z2                                                            
                                                                                                    #print(block)
                                                                                                    #print(long_F)
                                                                                                    if block>=long_F:
                                                                                                        Save=1
                                                                                                        #print(Save)
                                                                                                  
                                        
                                                                                               
                                                                                                                                                                                                                                                    
                                        
                                                                                    
                                                                                        #print(Z4)
                                                                                     
                            
                                                                                                                                                                                                                                
                                                                long_L=len(Z4)
                                                                                        #print(long_L)
                                                                if C9==0:
                                                                                 Z4=Z4[:long_L-En]
                                                                                 Z4+=Z2Z
                                                                                        
                                                                                            
                                                                N3=1
                                                                                        
                                                                                       
                                                                                        #print(N3)
                                                                                                                                                 
                                                                if N3==1:
                                                                                   N3=1
                                                                                  
                                                                                            
                                                                                   block=0
                                                                                   long_F=len(Z4)
                                                                                   Z=Z4
                                                                                   Z6=""
                                                                                   Z7=0
                                                                                   Z1=Z
                                                                                   cut_b=0
                            
                                                                                  
                                                                                
                                                                                  
                                                                                   
                                                                                   long_F=len(Z4)
                                                                                   while block<long_F:
                                                                                       E=Z[block:block+1]
                                                                                       
                                                                                       if E=="0" and Z7==0:
                                                                                           cut_b=1
                                                                                           block+=1
                                                                                           E2=Z[block:block+8]
                                                                                           block+=8
                                                                                           
                                                                                           E3=int(Z[block:block+5],2)
                                                                                           block+=5
                                                                                           E1=int(Z[block:block+E3],2)
                                                                                           block+=E3
                                                                                           E4=int(Z[block:block+5],2)
                                                                                           block+=5
                                                                                           E5=int(Z[block:block+E4],2)
                                                                                           block+=E4
                                                                                           b=0
                                                                                           E3=""
                                                                                           while b<E5-1:
                                                                                               
                                                                                               E3+=E2
                                                                                               b+=1
                                                                                               #print(E2)
                                                                                           Z1=Z1[block+1:] 
                                                                                           Z1=Z1[:E1]+E3+Z1[E1:]   
                                                                                       elif E=="1" or Z7==1:
                                                                                                block+=1
                                                                                                Z7=1 
                                                                                                
                                                                                                if cut_b==0:
                                                                                                    Z1=Z1[block:]
                                                                                                    cut_b=1
                                                                                                    #print(block)
                                                                                        
                                                                                               
                            
                            
                                                                                           #print(block)                                                    
                                                                                           
                                                                                           
                                                                                       
                                                                                       
                                                                                 
                                                                                 
                                                                                   
                                                                                 
                                                                                   #print(Long_PM1)
                                                                                   
                                                                                   Z4=Z1
                                                                                   #print(len(Z4))
                                                                                    
                                                                                   N3=1
                                                                                   Cot+=1
                                                                                   #print(Cot)
                                                                                   INFO=Z4
                                                                                   Extract1=0
                                                                                   N3=0
                                                                                   #print(len(Z4))
                                                                                   #print(Cot4)
                                                                                   if Cot==Cot4:
                                                                                       Extract1=1
                                                                                       N3=2
                                                                                       
                                                                                   if N3==2:
                                                                                       File_information5_17=Z4
                                                                                       long_1=len(File_information5_17)
                                                                                       add_bits=""
                                                                                       count_bits=8-long_1%8
                                                                                       z=0
                                                                                       if count_bits!=0:
                                                                                               while z<count_bits:
                                                                                                       add_bits="0"+add_bits
                                                                                                       z=z+1
                                                                                       File_information5_17=File_information5_17
                                                                                       if Extract1==1:                
                                                                                                L=len(File_information5_17)
                                                                                                n = int(File_information5_17, 2)
                                                                                                width_bits=len(File_information5_17)
                                                                                                width_bits=(width_bits//8)*2
                                                                                                width_bits=str(width_bits)
                                                                                                width_bits="%0"+width_bits+"x"
                                                                                                width_bits3=binascii.unhexlify(width_bits % n)
                                                                                                width_bits2=len(width_bits3)
                                                                                                File_information5_2=Clear
                                                                                             
                                                                                                jl=width_bits3
                                                                                                
                                                                                       
                                                                                               
                                                                                       
                                                                                                
                                                    
                                                                                                long=len(name)
                                                                                                name2=name[:long-2]
                                                                                                with open(name2, "wb") as f2:
                                                                                                    f2.write(width_bits3)
                                                                                                x2 = time()
                                                                                                x3=x2-x
                                                                                                xs=float(x3)
                                                                                                xs=str(xs)
                                                                                                return xs;                                                           
                                                            
                                                            
d=compression()
xw1=d.cryptograpy_compression4()
print(xw1)