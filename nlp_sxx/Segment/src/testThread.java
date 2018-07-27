import java.io.IOException;

/**
 *
 */


public class testThread  implements Runnable{
    private String name;
    private Object pre;
    private Object self;


    private testThread(String name,Object pre,Object self){
        this.name=name;
        this.pre=pre;
        this.self=self;
    }


    @Override
    public void run(){
        int count = 0;
        while(count<10){
            synchronized (pre) {
                synchronized (self) {
                    System.out.print(name);
                    count++;

                    self.notify();
                }
                try {
                    pre.wait();
                }catch (InterruptedException error){
                    error.printStackTrace();
                }

            }
        }
    }

public static void main(String args[])throws InterruptedException{
        Object a = new Object();
        Object b = new Object();
        Object c = new Object();
        testThread ThreadA = new testThread("A",c,a);
        testThread ThreadB = new testThread("B",a,b);
        testThread ThreadC = new testThread("C",b,c);


        new Thread(ThreadA).start();
        Thread.sleep(100);
        new Thread(ThreadB).start();
        Thread.sleep(100);
        new Thread(ThreadC).start();
        Thread.sleep(100);


    }



}
