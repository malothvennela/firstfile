class Stack:
    def_init_(self)
    self.stack=[]
    def push(self,item):
        self.stack.append(item)
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            return None
            def is_empty(self):
                return len(self.stack)==0
            def size(self):
                return len(self.stack)
            def reverse_sentence(sentence):
                stack=Stack()
            words=sentence.split()
            for word in words:
                stack.push(word)
            reversed_sentence += word + " "
            return
            reversed_sentence.strip()
            sentence = "name your is What"
            print("Original sentence:",sentence)
            print("Reversed sentence:",reverse_sentence(sentence))
