#pragma once
#include "LegacyDiagnosticTestFactory_Export.h"

#pragma warning( push )
#pragma warning( disable : 4251 )
namespace Diagnostics
{
class LEGACY_DIAGNOSTIC_TESTFACTORY_API HddpsTestList
{
public:
    static const std::string HddpsPciePresence;
    static const std::string HddpsPcieBer;
    static const std::string UsbPortReadWrite;
    static const std::string UsbBerPort;
    static const std::string HddpsSpiBer;
    static const std::string DpsDdr3DmaMemory;
    static const std::string HddpsDcNoGang;
    static const std::string HddpsDcGang;
    static const std::string HddpsAlarm;
    static const std::string HddpsAd5560Alarm;
    static const std::string HddpsDcGangIclamp;
    static const std::string HddpsInstrumentTempMonitoring;
    static const std::string HddpsLeakage;
    static const std::string HddpsCurrentSink;
    static const std::string HddpsTrigger;
    static const std::string HddpsSafeState;
    static const std::string HddpsDcCbg;
    static const std::string HddpsAirCoolScreening;
};
}
#pragma warning( pop )