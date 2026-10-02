class ReverseString {

    String reverse(String inputString) {
        String tmp = "";
        for( int i = inputString.length()-1; i>=0; i--){
            tmp += inputString.charAt(i);
        }
        return tmp;
    }
}