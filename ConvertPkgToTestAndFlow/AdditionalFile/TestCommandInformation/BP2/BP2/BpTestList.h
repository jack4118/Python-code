#pragma once

namespace Diagnostics
{
class BpTestList
{
public:
    static const std::string I2cPresenceTest;
    static const std::string Bp2I2cBerTest;
    static const std::string PcieDeviceCheckTest;
    static const std::string Bp2CheckVregSensor;
};
}