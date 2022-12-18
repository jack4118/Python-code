#pragma once
#include "LegacyDiagnosticTestFactory_Export.h"


#pragma warning( push )
#pragma warning( disable : 4251 )
namespace Diagnostics
{
class LEGACY_DIAGNOSTIC_TESTFACTORY_API TcTestList
{
public:
    static const std::string UeiUartExternalLoopbackTest;
    static const std::string UeiTestExternalLoopbackSideband;
    static const std::string PSRamTest;
    static const std::string PowerSumTest;
    static const std::string TDAUtemperature;
};
}
#pragma warning( pop )