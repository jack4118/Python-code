#pragma once

namespace Diagnostics
{
class PseTestList
{
public:
    static const std::string PseCheckVregSensor;
    static const std::string PseI2cPresenceTest;
    static const std::string Pse6kwI2cPresenceTest;
    static const std::string Pse6kwI2cBERTest;
    static const std::string Pse6kwDeltaBpsI2cPresenceTest;
    static const std::string Pse6kwDeltaBpsI2cBERTest;
    static const std::string Pse6kwVregTest;
    static const std::string Pse6kwPwrModuleMfgRegTest;
    static const std::string Pse6kwPwrModuleRegTest;
};
}