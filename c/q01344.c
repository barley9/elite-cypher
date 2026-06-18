/*
 * 1344. Angle Between Hands of a Clock
 * 
 * Given two numbers, `hour` and `minutes`, return the smaller angle (in degrees)
 * formed between the hour and the minute hand.
 * 
 * Answers within `10^-5` of the actual value will be accepted as correct.
 */

#include <math.h>

double angleClock(int hour, int minutes) {
    /* O(1) time, O(1) space solution */
    double t, theta_m, theta_h, dtheta;

    t = hour + ((double) minutes / 60);
    theta_m = (360 * t) / 1;
    theta_h = (360 * t) / 12;
    dtheta = fmod((theta_m - theta_h), 360);

    if (dtheta < 360 - dtheta) {
        return dtheta;
    } else {
        return 360 - dtheta;
    }
}