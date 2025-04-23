/*
 * Simulation.java
 * last edited 250422 gggentooo
 * 
 * wrapper class for all simulation related tasks
 */

package umaengine.simulation;

import umaengine.obj.Race;

public class Simulation {
    private Race race;

    public Simulation(short race_id) {
        this.race = new Race(race_id);
    }
}
