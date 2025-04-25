/*
 * Race.java
 * 250422 gggentooo
 */

package umaengine.obj;

public class Race {
    // 마장 유형: 잔디, 더트
    public enum FieldType {
        TURF, DIRT
    }

    // 회전 방향: 시계(우), 반시계(좌) 
    public enum Direction {
        CLOCKWISE, COUNTERCLOCKWISE
    }

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
