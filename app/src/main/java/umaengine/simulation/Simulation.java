/*
 * Simulation.java
 * last edited 250422 gggentooo
 * 
 * wrapper class for all simulation related tasks
 */

package umaengine.simulation;

import umaengine.obj.Race;

public class Simulation {
    private final Race race;

    public Simulation(short race_id) {
        race = new Race(race_id);
    }
}
