#pragma once

namespace Diagnostics
{
class RcTestList
{
public:
    static const std::string Rc2I2cPresenceTest;
    static const std::string PciePresenceTest;
    static const std::string Rc2PcieBERTest;
    static const std::string UsbPortReadWriteTest;
    static const std::string Rc2UsbBerTest;
    static const std::string RcFpgaSramTest;
    static const std::string Rc2RefClkPllTest;
    static const std::string Rc2OcxoOscillatorTest;
    static const std::string Gpio;
    static const std::string Rc2VRegTest;
    static const std::string TriggerTest;
    static const std::string FpgaRcTempTest;
};
}