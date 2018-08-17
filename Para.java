import java.util.*;
class Par{
	
	Stack<Character> stack=new Stack<>();
	boolean flag;
	
	Par(){
		stack=new Stack<>();
		flag=true;

	}
	
	public int check(String str){
		char ch;
		//boolean flag=true;
		for(int i=0;i<str.length();i++){
				ch=str.charAt(i);
				//boolean flag=true;
				if(ch==')'){
					char top=stack.peek();
					stack.pop();
					 flag=true;
					while(top!='('){
						if(top == '*'||top == '+'||top== '-'||top == '/'){
							flag=false;
						}
						top=stack.peek();
						stack.pop();
					}
					if(flag==true)
						return 1;
				}
				
			else{
				stack.push(ch);
			}
			
		}
	return 0;
	}
}
	class Para{
		public static void main(String[] args) {
		
			Par p = new Par();
			String s = "(a+(a+b))";
			System.out.println(p.check(s));
		}
	}