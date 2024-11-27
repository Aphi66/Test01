public class test {
    public static int waterM,electM;
    public static int resultBill;

    public static int currentwatermeter, lastwatermeter;
    public  static int currentelectmeter, lastelectmeter;

    public static int calculatewaterBill () {
        if (currentwatermeter >= lastwatermeter){
            waterM = (currentwatermeter-lastwatermeter)*5;
        }
        return waterM;
    }

    public  static int calculaterelectBill (){
        if (currentelectmeter >= lastelectmeter) {
            electM = (currentelectmeter-lastelectmeter)*6;
        }
        return electM;
    }

    public static int calculaterresultBill (String roomType){
        if (roomType.equals("s")) {
            resultBill = 1500+ calculaterelectBill() + calculatewaterBill();
        }else if (roomType.equals("D")){
            resultBill = 2000+ calculaterelectBill()+ calculatewaterBill();
            
        }
        return resultBill;
    }
    public static void main(String[] args) {
        currentelectmeter =50;
        lastelectmeter =20;

        currentwatermeter = 100;
        lastwatermeter =50 ;

        System.out.println("You bill is:" + calculaterresultBill("D"));
    }
}