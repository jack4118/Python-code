#pragma once
#include "LegacyDiagnosticTestFactory_Export.h"

#pragma warning( push )
#pragma warning( disable : 4251 )
namespace Diagnostics
{
class LEGACY_DIAGNOSTIC_TESTFACTORY_API HpccTestList
{
public:
    static const std::string VsvmPathResistanceTest;
    static const std::string HpccPciePresence;
    static const std::string HpccPcieBerTest;
    static const std::string HpccPcieLinkSpeedTest;
    static const std::string HpccDdr3MemoryTest;
    static const std::string HpccVsvmLoopbackTest;
    static const std::string VsvmSecondaryLoopbackTest;
    static const std::string HpccVsimTest;
    static const std::string HpccIsvmTest;
    static const std::string HpccVclampTest;
    static const std::string HpccIclampTest;
    static const std::string HpccPmuTrigger;
    static const std::string HpccVimpedanceTest;
    static const std::string HpccVixTest;
    static const std::string HpccIoxTest;
    static const std::string HpccVoxTest;
    static const std::string HpccTermVrefTest;
    static const std::string HpccVrefAccuracyTest;
    static const std::string Hpcc2TriggerTest;
    static const std::string HpccSpiTest;
    static const std::string HpccSeDriverSkewAndJitter;
    static const std::string HpccSeComparatorSkewAndJitter;
    static const std::string HpccEpa;
    static const std::string HpccSlewRateTest;
    static const std::string HpccTimingRegression;
    static const std::string HpccAdate320TempSensorTest;
};
}
#pragma warning( pop )
