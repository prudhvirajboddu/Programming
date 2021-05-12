def designerPdfViewer(h, word):
    return(len(word) * max([h[ord(i)-97] for i in word]))
    #since input is of lowercase letters have to find maximum of h from 
    #the word have to subtract with ascii value of 'a'
    
print(designerPdfViewer([1,3,1,3,1,4,1,3,2,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5],'abc'))