/*
 * Race.java
 * 250422 gggentooo
 */

package umaengine.obj;

public class Race {
    private short id;
    private String name;

    public Race(int race_id) {
        id = 0;
    }

    public void setNum(short s) {
        id = s;
    }

    public void setName(String n) {
        name = n;
    }

    public short returnNum() {
        return id;
    }

    public String returnName() {
        return name;
    }
}
