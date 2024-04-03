#on this project I learned the concept of brace mapping
#this also moment o also learned more on generator 


from time import time,sleep#utilities
speed = 0xffffff#the update/second

class brainoof:#class cus I want organized code :)
    @staticmethod #static cus y not
    def run(code:str) -> None:
        """simulate brainoof"""
        #registers
        stacknum = 50
        insptr,cellptr,stck = 0,0,[0]*stacknum
        #load working variables 
        code = brainoof.clean2(code)
        out,cycles = "",0
        bmap = brainoof.bmapcreate(code)
        #infini for loop
        print(stck[0])
        for _ in iter(int,1):
            cycles+=1
            n1 = time()
            ins = code[insptr]

            #will create the pointed code for visuality 
            tOut=""
            tempcode = dcopy(code)
            for i in range(len(tempcode)):
                if i == insptr:tOut+="{"
                tOut+=tempcode[i]
                if i == insptr:tOut+="}"
                

            #the brainOof main workings
            if ins == "+":stck[cellptr] = 0 if stck[cellptr] > 255 else stck[cellptr]+1
            if ins == "-":stck[cellptr] = 255 if stck[cellptr] <= 0 else stck[cellptr]-1
            if ins == ">":cellptr = 0 if cellptr >= stacknum-1 else cellptr+1
            if ins == "<":cellptr = stacknum-1 if cellptr <= 0 else cellptr-1
            if ins == "[" and stck[cellptr] == 0:insptr = bmap[insptr]
            if ins == "]" and stck[cellptr] != 0:insptr = bmap[insptr]
            if ins == ".":
            	"""print(chr(stck[cellptr]),end="")"""
            	out+=chr(stck[cellptr])
            if ins == ",":stck[cellptr] = ord(input(">>>"))
            #step on next instruction 
            insptr+=1
            
            #will create the pointed cell for visuality 
            t=""
            j=0
            
            for i in range(len(stck)):
                if i not in [cellptr+1,cellptr]:
                    t+="|"
                if i == cellptr:t+="{"
                t+=("0"*(3-len(str(stck[i]))))+str(stck[i])#must always show 3 digit decimal
                if i == cellptr:t+="}"
                
                j+=1
                if j>13:
                	j=0
                	t+="\n"
                	
            #visualize everything 
            print(cellptr)
            print("\x1b[;H\x1b[J"+tOut+"\n>>>"+out,
            f"\ninsno#{insptr} \ncellno#{cellptr} = {stck[cellptr]} \nsteps {cycles} \n{t}")
            #the looping condition 
            
            if len(code) <= insptr:break
			#to keep it over speeding 
            sleep(max(0,1/speed-(time()-n1)))
		#this is just my choice so don't bother me about this
        return out, cycles

    @staticmethod
    def clean(code:str) -> str:
        """remove all non brainoof's code"""
        temp=""
        for i in code:
            if i in "+-><,.[]":
                temp+=i
        return temp
    @staticmethod
    def clean2(code:str) -> str:#i just stole this since I find this looks better
    	return ''.join(filter(lambda x: x in "><[],.+-", code))


    @staticmethod
    def bmapcreate(code:str) -> list:
        """return a brace map"""
        tempbmap,bmap = [],[0]*len(code)
        for address,char in enumerate(code):
            if char == "[": #create head 
                tempbmap+=[address]
            if char == "]":#create tail for brace
                head=tempbmap.pop()
                bmap[head]=address
                bmap[address]=head
        return bmap

#just a helper function cus y not
def dcopy(lis:list) -> "copy of the given list":
    return [i for i in lis]

#idk y I have to make sure it's running on __main__ but someone say it's important
#so I just followed it
if __name__ == "__main__":
    #hello worlds variations 
    a = "++++++++[>++++[>++>+++>+++>+<<<<-]>+>+>->>+[<]<-]>>.>---.+++++++..+++.>>.<-.<.+++.------.--------.>>+.>++,"
    b = "+[-->-[>>+>-----<<]<--<---]>-.>>>+.>>..+++[.>]<<<<.+++.------.<<-.>>>>+."
    c = "++++++++++[>+++++++>++++++++++>+++>+<<<<-]>++.>+.+++++++..+++.>++.<<+++++++++++++++.>.+++.------.--------.>+.>."
    d = """>++++[-<+++++++++++>]>-[[->+>+<<]>[-<+>]+>-]<-<-<[-<[[->>+>>+<<<<]>>>>[>>>>++++++++++<
<<<[->+>>+>-[<-]<[->>+<<<<[->>>+<<<]>]<<]>+[-<+>]>>>[-]>[-<<<<+>>>>]<<<<]<[>++++++[<++
++++++>-]<-.[-]<]<<<<[<<]<.>>>[>>]>[->+>>+<<<]>[-<+>]<<<<[-<[->>+<<]>>>+[>>]+<-[>-]>[-
<<[<<]>[-]>[>>]>>[-<+<<+>>>]<[->+<]]<<<[<<]<<]>>>>[-<[-<<+>>]<+>>>>]>>[-]<<<[-]<<]<]"""
    e = ">,[>++++++[-<-------->]>+++++++++[<<<[->+>+<<]>>[-<<+>>]>-]<<[-<+>],]<"
    f = " >,[>++++++[-<-------->]>+++++++++[<  read number<<[->+>+<<]>>[-<<+>>]>-]<<[-<+>],]<  ** part 2 **"
    print([brainoof.run(code) for code  in [a]])#generator cus yeah to run multiple code ones but add "," on the last of the code to see the output
